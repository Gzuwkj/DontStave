from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class book(models.Model):
    bf = HTMLField(blank=True, default='')
    bn = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.bf


class Auth(models.Model):
    book = models.ForeignKey(to=book, on_delete=models.CASCADE, default='')
    name = HTMLField(blank=True, default='')
