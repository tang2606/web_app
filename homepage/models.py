from django.db import models

# Create your models here.



class Homepage(models.Model):
    description = models.CharField(max_length=150)

