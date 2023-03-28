from django.urls import path
from . import views

urlpatterns = [
    path("", views.FoodFact.as_view())
]
