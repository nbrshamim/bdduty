from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('totalduty', views.totalduty, name='totalduty'),
]
