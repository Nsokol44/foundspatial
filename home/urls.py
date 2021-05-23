from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name="home-main"),
    path('about/', views.about_view, name="about-main")
]
