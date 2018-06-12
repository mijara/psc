from django.db import models
from django.urls import reverse_lazy
import pandas as pd


FORMAT_CSV = 1


class Dataset(models.Model):
    name = models.CharField(
        max_length=256
    )

    file = models.FileField()

    format = models.IntegerField(
        choices=(
            (FORMAT_CSV, 'csv'),
        )
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('datasets:dataset_detail', args=[self.pk])

    def get_table(self):
        if self.format == FORMAT_CSV:
            df = pd.read_csv(self.file)
        else:
            df = None

        return df
