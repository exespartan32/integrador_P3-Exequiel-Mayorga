from django.urls import path
from . import views

urlpatterns = [
    path('', views.diario, name='diario'),
]
