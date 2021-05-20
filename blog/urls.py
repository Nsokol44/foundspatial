from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('search/', views.blog_view, name='blog-search'),
    path('post/<slug:slug>/', views.detail_view, name='detail'),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),
]
