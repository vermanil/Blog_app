from __future__ import unicode_literals

from django.db import models



# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    Date = models.DateTimeField()
    Image = models.ImageField()
    Content = models.TextField()