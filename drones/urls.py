from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.drone_view, name='drone-home'),
    path('droneshot/<slug:slug>/', views.drone_detail, name='drone-detail'),
]
