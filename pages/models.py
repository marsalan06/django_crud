from django.db import models

# Create your models here.
class Contact_Model(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=255)
    name=models.CharField(max_length=255, null=True)
    
    objects=models.manager