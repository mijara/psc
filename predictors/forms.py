from django import forms
from . import models
from datasets.models import Dataset


class ScikitMLPPredictorForm(forms.ModelForm):
    class Meta:
        model = models.ScikitMLPPredictor
        fields = ('name', 'solver', 'alpha', 'layers')


class TrainForm(forms.Form):
    dataset = forms.ModelChoiceField(Dataset.objects)
