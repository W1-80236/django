from django.db import models

# Create your models here.
class Registrationform(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    date = models.DateField()
    dob=models.DateField(auto_created=True)
