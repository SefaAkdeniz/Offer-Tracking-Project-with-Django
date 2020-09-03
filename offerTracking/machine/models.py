from django.db import models

# Create your models here.

class Machine(models.Model):
    machine_name = models.CharField(max_length=100, verbose_name="Tezgah Adı")


    def __str__(self):
        return self.machine_name

    class Meta:
        verbose_name = 'Tezgah'
        verbose_name_plural = 'Tezgahlar'


    
