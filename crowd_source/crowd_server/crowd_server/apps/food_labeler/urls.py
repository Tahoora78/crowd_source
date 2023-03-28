from django.urls import path
from . import views


urlpatterns = [
    path('', views.FoodLabelerView.as_view()),
]
