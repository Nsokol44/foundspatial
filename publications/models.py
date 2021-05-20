from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    pubImage = models.ImageField(blank=True, null=True, upload_to='pub_images')
    datetime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title
