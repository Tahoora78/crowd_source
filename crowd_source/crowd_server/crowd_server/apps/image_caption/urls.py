from django.urls import path
from . import views


urlpatterns = [
    path('', views.ImageCaption.as_view(), name="image_caption")
]
