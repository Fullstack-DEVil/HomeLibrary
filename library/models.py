import random
from django.db import models

# Create your models here.
def generate_unique_id():
    while True:
        new_id = str(random.randint(10000, 999999))
        if not Book.objects.filter(id=new_id).exists():
            return new_id

class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=6, default=generate_unique_id, editable=False)
    title = models.CharField(max_length=100)
    isbn_10 = models.CharField(max_length=10, blank=True, null=True)
    isbn_13 =models.CharField(max_length=13, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    publish_date = models.CharField(max_length=20)
    cover_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} | {self.id}'