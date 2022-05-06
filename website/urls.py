from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.LCproductAPI.as_view()),
    path( 'products/<int:pk>/', views.RUDproductAPI.as_view()),

    ]
