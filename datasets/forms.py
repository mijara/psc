from django import forms
from . import models


class DatasetForm(forms.ModelForm):
    class Meta:
        model = models.Dataset
        fields = ('name', 'file', 'format')
