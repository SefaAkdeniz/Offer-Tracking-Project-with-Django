# Generated by Django 3.0.8 on 2020-09-03 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0004_auto_20200903_2003'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interviews_type', models.PositiveSmallIntegerField(choices=[(1, 'Karşı Taraf Arama'), (2, 'Haksan Taraf Arama'), (3, 'E-Posta'), (4, 'Mağazaya Geldi')], verbose_name='Görüşme Tipi')),
                ('note', models.TextField(verbose_name='Görüşme Notu')),
                ('offer_date', models.DateTimeField(auto_now_add=True, verbose_name='Görüşme Tarihi')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer', verbose_name='Firma')),
                ('personel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sorumlu Personel')),
            ],
            options={
                'verbose_name': 'Görüşme',
                'verbose_name_plural': 'Görüşmeler',
            },
        ),
    ]
