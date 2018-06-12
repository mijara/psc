from django.contrib import admin
from django.urls import path
from . import views

app_name = 'predictors'

urlpatterns = [
    path(
        'create/scikitmlppredictor/',
        views.ScikitMLPPredictorCreateView.as_view(),
        name='scikitmlppredictor_create'
    ),

    path(
        '',
        views.PredictorListView.as_view(),
        name='predictor_list'
    ),

    path(
        '<int:pk>/',
        views.PredictorDetailView.as_view(),
        name='predictor_detail'
    ),
]
