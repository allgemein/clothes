from django.urls import path

from . import views

urlpatterns = [
    path('', views.shoot, name='shoot'),
]
