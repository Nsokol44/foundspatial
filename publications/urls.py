from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.publication_home, name='publication-home'),
]
