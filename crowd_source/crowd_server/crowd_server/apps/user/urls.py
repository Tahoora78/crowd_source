from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import UserAPIView, RegisterAPIView, LoginAPIView
from knox.views import LogoutView


urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPIView.as_view()),
    path('login', LoginAPIView.as_view(), name='login'),
    path('register', RegisterAPIView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='knox_logout'),
    ]


