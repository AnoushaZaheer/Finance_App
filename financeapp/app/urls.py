from django.urls import path
from app import views
from .views import *
urlpatterns = [
    path('', views.home,name='home'),
]
