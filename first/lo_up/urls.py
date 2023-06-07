from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("login/", views.Login, name = "login"),
    path("signup/", views.SignUp, name = "signup"),
    path("dashboard/", views.Dashboard, name = "dashboard"),
    path("upload/", views.Upload, name = "upload"),
    path("search/", views.QuestionList, name='search'),

    # path("reward/", views.Reward, name='reward'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
