
from django.urls import path
from . import views



urlpatterns = [
    path("rew", views.customer, name = "review"),
]