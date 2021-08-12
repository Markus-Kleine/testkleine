from django.db import models

# Create your models here.
class PersonModell(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Artikel(models.Model):
    matnr = models.CharField(max_length=18, primary_key=True)
    maktx_1 = models.CharField(max_length=40)
    maktx_2 = models.CharField(max_length=40)
    lifnr = models.CharField(max_length=10)
    aritkelbild = models.ImageField(upload_to="upload")




