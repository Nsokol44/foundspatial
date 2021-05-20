from django.db import models

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='resource_files')
