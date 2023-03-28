from django.urls import path
from . import views

urlpatterns = [
    path("", views.Sentiment.as_view())
]
