from django.db import models

# Create your models here.

class Lostitems(models.Model):
    date = models.DateField()
    name = models.CharField(max_length = 200)
    details = models.TextField()