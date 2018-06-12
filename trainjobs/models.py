import pickle
import uuid
from random import choice

import numpy as np
from django.db import models
from django.urls import reverse_lazy


def split_data(x, y, split):
    length = int(len(x) * split / 100.0)

    random_indices = np.arange(0, x.shape[0])
    np.random.shuffle(random_indices)

    train_indices = random_indices[:length]
    test_indices = random_indices[length:]

    x_train = x[train_indices]
    y_train = y[train_indices]

    x_test = x[test_indices]
    y_test = y[test_indices]

    return x_train, y_train, x_test, y_test


class TrainJob(models.Model):
    predictor = models.ForeignKey('predictors.Predictor', on_delete=models.CASCADE)

    dataset = models.ForeignKey('datasets.Dataset', on_delete=models.CASCADE)

    name = models.CharField(max_length=256)

    target = models.CharField(max_length=128)

    state_pickle = models.FileField()

    def save(self, *args, **kwargs):
        # get train data.
        dataset = self.dataset.get_table()
        y = dataset[self.target].as_matrix()
        x = dataset.drop([self.target], 1).as_matrix()
        x_train, y_train, x_test, y_test = split_data(x, y, 75)

        # train the predictor.
        predictor = self.predictor.get_child()
        state = predictor.train(x_train, y_train)

        # save state to a file.
        file_path = f'predictor_{str(uuid.uuid4())}.pickle'
        with open(file_path, 'wb') as f:
            pickle.dump(state, f)
        self.state_pickle = file_path

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('trainjobs:trainjob_detail', args=[self.pk])

    def get_sample_row(self):
        dataset = self.dataset.get_table()
        x = dataset.drop([self.target], 1).as_matrix()

        return ','.join(map(str, choice(x)))
