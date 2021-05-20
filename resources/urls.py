from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.resource_home, name='resource-home'),
]
