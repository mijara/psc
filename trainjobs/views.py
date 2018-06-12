import pickle

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic

from predictors.models import Predictor
from . import models, forms


class TrainJobCreateView(generic.CreateView):
    model = models.TrainJob
    form_class = forms.TrainJobForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        if 'p' in self.request.GET:
            form.fields['predictor'].initial = get_object_or_404(Predictor, pk=self.request.GET['p'])
        return form


class TrainJobDetailView(generic.DetailView):
    model = models.TrainJob


class TrainJobPredictView(generic.DetailView):
    model = models.TrainJob

    def get(self, request, *args, **kwargs):
        # get row.
        row = self.request.GET['p']
        row = row.split(',')
        row = list(map(float, row))

        with open(self.get_object().state_pickle.path, 'rb') as f:
            clf = pickle.load(f)

        result = clf.predict([row])

        return HttpResponse(str(result[0]))
