from django.contrib import admin
from django.urls import path
from . import views

app_name = 'predictors'

urlpatterns = [
    path(
        'create/',
        views.DatasetCreateView.as_view(),
        name='dataset_create'
    ),

    path(
        '',
        views.DatasetListView.as_view(),
        name='dataset_list'
    ),

    path(
        '<int:pk>/',
        views.DatasetDetailView.as_view(),
        name='dataset_detail'
    ),
]
