import uuid

from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn_10 = models.CharField(max_length=10, blank=True, null=True)
    isbn_13 =models.CharField(max_length=13)
    description = models.TextField(null=True, blank=True)
    publish_date = models.CharField(max_length=20)
    cover_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} | {self.id}'