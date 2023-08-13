from django.urls import path

from . import views

urlpatterns = [
    path("", views.service, name="service"),
    path("status/", views.status, name="status")
]