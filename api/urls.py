from django.conf.urls import include, url
from django.contrib import admin

from .v1 import urls as v1

urlpatterns = [
    url(r'^v1/', include(v1)),
]
