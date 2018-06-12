import numpy as np
from django.core import validators
from django.db import models
from django.urls import reverse_lazy
from sklearn.neural_network import MLPClassifier


class Predictor(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_child(self):
        if hasattr(self, 'scikitmlppredictor'):
            return self.scikitmlppredictor

    def train(self, x, y):
        raise NotImplementedError()

    def predict(self):
        raise NotImplementedError()

    def get_absolute_url(self):
        return reverse_lazy('predictors:predictor_detail', args=[self.pk])


class ScikitMLPPredictor(Predictor):
    solver = models.CharField(
        choices=(
            ('lbfgs', 'lbfgs'),
        ),
        max_length=32,
    )

    alpha = models.FloatField()

    layers = models.CharField(
        validators=[validators.validate_comma_separated_integer_list],
        max_length=512,
    )

    def predict(self):
        pass

    def train(self, x, y):
        clf = MLPClassifier(
            solver=self.solver,
            alpha=self.alpha,
            hidden_layer_sizes=list(map(int, self.layers.split(','))),
            random_state=1,
            verbose=True
        )

        return clf.fit(x, np.round(y))
