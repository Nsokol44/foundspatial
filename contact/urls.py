from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signUp, name='contact-page'),
    path('success/', views.successSignUp, name='post-sign-up'),
]
