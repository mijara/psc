from django import forms
from . import models


class TrainJobForm(forms.ModelForm):
    class Meta:
        model = models.TrainJob
        fields = ('name', 'predictor', 'dataset', 'target')
