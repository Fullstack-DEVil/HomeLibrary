from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.CharField(max_length=20)
    isbn = models.CharField(max_length=13)
    description = models.TextField(null=True, blank=True)
    cover_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} | {self.isbn}'