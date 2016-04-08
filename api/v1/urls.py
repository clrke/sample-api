from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^messages/(?P<id>\d+)', views.message),
    url(r'^messages', views.messages),
]
