
from django.contrib import admin
from django.urls import path

from courseapp import views

urlpatterns = [
    path("", views.home),
    path("delete/<int:id>/",views.delete)
]