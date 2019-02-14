from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length = 100)
    harga = models.TextField(max_length = 100)
    gambar = models.ImageField(upload_to='blog')

    def __str__(self):
        return self.nama