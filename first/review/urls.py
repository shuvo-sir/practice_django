
from django.urls import path
from . import views



urlpatterns = [
    path("rew", views.customer, name = "review"),
    path("build/", views.building_form, name = "registration"),
    path("login/", views.login_form, name = "login"),
    path("success/", views.login_success),
]