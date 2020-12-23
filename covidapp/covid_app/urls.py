from django.contrib import admin
from django.urls import path
from .views import reportView

urlpatterns = [
    path('', reportView)
]
