from django.urls import path
from . import views

urlpatterns = [
    path("", views.papers, name="about"),
    path("papers/", views.papers, name="papers"),
    path("contact/", views.contact, name="contact"),
]
