from django.urls import path

from . import views

urlpatterns = [
    path('shoot/', views.shoot, name='shoot'),
]
