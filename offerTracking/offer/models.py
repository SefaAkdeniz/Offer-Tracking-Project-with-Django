from django.db import models
from customer.models import Customer

# Create your models here.


class Offer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Firma')
    personel = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name='Sorumlu Personel')
    offer_file = models.FileField(upload_to='uploads/%Y/%m/%d/')