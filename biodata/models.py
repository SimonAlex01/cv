from django.db import models

class BioData(models.Model):
    dob = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)