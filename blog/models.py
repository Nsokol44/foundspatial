from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=80)
    datetime = models.DateTimeField(auto_now_add=False)
    title = models.CharField(max_length=500)
    description = models.TextField()
    post = models.TextField()
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()
    published = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    link = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        """
        Set publish date to the date when post's published status is switched to True,
        reset the date if post is unpublished
        """
        if self.published and self.datetime is None:
            self.datetime = datetime.now()
        elif not self.published and self.datetime is not None:
            self.datetime = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
     return reverse('detail', kwargs={'slug': self.slug})
