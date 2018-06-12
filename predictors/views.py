from django.views import generic

from . import forms, models


class ScikitMLPPredictorCreateView(generic.CreateView):
    form_class = forms.ScikitMLPPredictorForm
    model = models.ScikitMLPPredictor


class PredictorListView(generic.ListView):
    model = models.Predictor


class PredictorDetailView(generic.DetailView):
    model = models.Predictor
