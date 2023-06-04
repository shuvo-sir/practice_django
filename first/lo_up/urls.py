from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path("login/", views.Login, name = "login"),
    path("signup/", views.SignUp, name = "signup"),
    # path("dashboard/", views.Dashboard, name = "dashboard"),
    path("dashboard2/", views.Dashboard2, name = "dashboard2"),
    path("upload/", views.Upload, name = "upload"),
]