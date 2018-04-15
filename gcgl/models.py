from django.db import models

# Create your models here.

class Pj(models.Model):
    pj=models.CharField(max_length=32)
    pname=models.CharField(max_length=32)
