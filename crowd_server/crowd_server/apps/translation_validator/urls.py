from django.urls import path
from . import views


urlpatterns = [
    path('', views.TranslationValidatorView.as_view()),
]
