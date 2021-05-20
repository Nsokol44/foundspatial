from django.contrib import admin
from .models import DroneFootage


@admin.register(DroneFootage)
class DroneAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'post', 'slug', 'published', 'droneImage', 'droneVideo')
