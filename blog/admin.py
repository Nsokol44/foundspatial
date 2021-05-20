from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'post', 'slug', 'tags', 'published', 'image', 'link')
