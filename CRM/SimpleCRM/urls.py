from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('sign-up',views.sign_up)
]