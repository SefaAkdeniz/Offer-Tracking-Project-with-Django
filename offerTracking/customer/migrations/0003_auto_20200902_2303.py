# Generated by Django 3.0.8 on 2020-09-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200902_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='company_city',
            field=models.PositiveSmallIntegerField(choices=[(6, 'ANKARA'), (34, 'İSTANBUL'), (35, 'İZMİR'), (17, 'ÇANAKKALE')], verbose_name='Konum'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'İş Makinesi Üreticileri'), (2, 'İstif Makineleri Üreticileri'), (3, 'Tarım Makinaları Üreticileri'), (4, 'Hidrolik Pnömatikçiler')], verbose_name='Firma İş Alanı'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_contact',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Refarans Tavsiyesi'), (2, 'Sosyal Medya'), (3, 'Mağaza Ziyareti'), (4, 'E-Mail'), (5, 'Telefon Araması'), (6, 'Diğer')], verbose_name='İlk İletişim'),
        ),
    ]
