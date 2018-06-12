from django.views import generic
from . import models, forms


class DatasetCreateView(generic.CreateView):
    model = models.Dataset
    form_class = forms.DatasetForm


class DatasetListView(generic.ListView):
    model = models.Dataset


class DatasetDetailView(generic.DetailView):
    model = models.Dataset
