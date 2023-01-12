from django.db import models

# Create your models here.
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    description = models.CharField(max_length=30000000)
    video = EmbedVideoField()

class Video(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=30000000)
    video = models.FileField(upload_to="img", default='')
    def __str__(self):
        return self.title