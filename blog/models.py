from __future__ import unicode_literals

from django.db import models



# Create your models here.
class Article(models.Model):
    title = models.CharField()
    author = models.CharField()
    Date = models.DateTimeField()
    Image = models.CharField()
    Content = models.TextField()