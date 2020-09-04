from django.db import models
from offer.models import Offer


# Create your models here.

TYPE_CHOICES = (
    (1, 'Karşı Taraf Arama'),
    (2, 'Haksan Taraf Arama'),
    (3, 'E-Posta'),
    (4, 'Mağazaya Geldi'),  
)

class Interviews(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, verbose_name='Teklif')
    personel = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name='Sorumlu Personel')
    interviews_type = models.PositiveSmallIntegerField( choices=TYPE_CHOICES, verbose_name="Görüşme Tipi")
    note = models.TextField(verbose_name="Görüşme Notu")
    offer_date = models.DateTimeField(auto_now_add=True, verbose_name="Görüşme Tarihi")

    def __str__(self):
        return self.offer.customer.company_name

    class Meta:
        verbose_name = 'Görüşme'
        verbose_name_plural = 'Görüşmeler'


