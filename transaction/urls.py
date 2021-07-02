from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('complete/', views.paymentComplete, name="complete"),

]
