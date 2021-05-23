from django.contrib import admin
from .models import Bio

# Register your models here.



@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'bioImage', 'bioDesc', 'datetime')
