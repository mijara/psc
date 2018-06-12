from django.contrib import admin
from django.urls import path
from . import views

app_name = 'trainjobs'

urlpatterns = [
    path(
        'create/',
        views.TrainJobCreateView.as_view(),
        name='trainjob_create'
    ),

    path(
        '<int:pk>/',
        views.TrainJobDetailView.as_view(),
        name='trainjob_detail'
    ),

    path(
        '<int:pk>/predict/',
        views.TrainJobPredictView.as_view(),
        name='trainjob_predict'
    ),
]
