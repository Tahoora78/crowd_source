from django.urls import path
from . import views


urlpatterns = [
    path('', views.FoodCompare.as_view(), name="image_caption")
]
