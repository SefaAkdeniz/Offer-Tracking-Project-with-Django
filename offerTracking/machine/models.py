from django.db import models

# Create your models here.

class Machine(models.Model):
    machine_name = models.CharField(max_length=100, verbose_name="Tezgah Adı")
    
