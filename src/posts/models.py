from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField

from users.models import UserProfile


class Post(models.Model):
    image = ThumbnailerImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = HTMLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
