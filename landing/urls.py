from django.contrib import admin
from django.urls import path
from . import views

app_name = 'predictors'

urlpatterns = [
    path(
        '',
        views.LandingView.as_view(),
        name='landing'
    ),
]
