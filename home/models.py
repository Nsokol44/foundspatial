from django.db import models

# Create your models here.

class Bio(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bioImage = models.ImageField(blank=True, null=True, upload_to='bioImages')
    bioDesc = models.TextField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title
