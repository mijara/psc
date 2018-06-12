from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from collahuasa import settings

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include(
            'landing.urls',
            namespace='landing'
        )
    ),

    path(
        'predictors/',
        include(
            'predictors.urls',
            namespace='predictors'
        )
    ),

    path(
        'datasets/',
        include(
            'datasets.urls',
            namespace='datasets'
        )
    ),

    path(
        'trainjobs/',
        include(
            'trainjobs.urls',
            namespace='trainjobs'
        )
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
