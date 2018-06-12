from django.shortcuts import render
from django.views import generic


# Create your views here.
from datasets.models import Dataset
from predictors.models import Predictor


class LandingView(generic.View):
    def get(self, request, *args, **kwargs):
        predictors = Predictor.objects.all()
        datasets = Dataset.objects.all()

        return render(request, 'landing/landing.html', {
            'predictors': predictors,
            'datasets': datasets,
        })
