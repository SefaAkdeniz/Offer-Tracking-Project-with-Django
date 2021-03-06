# Generated by Django 3.0.8 on 2020-09-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='company_city',
            field=models.PositiveSmallIntegerField(choices=[(6, 'ANKARA'), (34, 'İSTANBUL'), (35, 'İZMİR'), (17, 'ÇANAKKALE')], max_length=100, verbose_name='Konum'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'İş Makinesi Üreticileri'), (2, 'İstif Makineleri Üreticileri'), (3, 'Tarım Makinaları Üreticileri'), (4, 'Hidrolik Pnömatikçiler')], max_length=100, verbose_name='Firma İş Alanı'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_contact',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Refarans Tavsiyesi'), (2, 'Sosyal Medya'), (3, 'Mağaza Ziyareti'), (4, 'E-Mail'), (5, 'Telefon Araması'), (6, 'Diğer')], max_length=100, verbose_name='İlk İletişim'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_contact_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='İlk İlişki Tarihi'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='related_person_mail1',
            field=models.CharField(max_length=100, null=True, verbose_name='1.İlgili Kişi E-Posta Adresi'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='related_person_mail2',
            field=models.CharField(max_length=100, null=True, verbose_name='2.İlgili Kişi E-Posta Adresi'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='related_person_name1',
            field=models.CharField(max_length=100, null=True, verbose_name='1.İlgili Kişi Adı'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='related_person_name2',
            field=models.CharField(max_length=100, null=True, verbose_name='2.İlgili Kişi Adı'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='related_person_phone1',
            field=models.CharField(max_length=11, null=True, verbose_name='1.İlgili Kişi Cep Telefon Numarası'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='related_person_phone2',
            field=models.CharField(max_length=11, null=True, verbose_name='2.İlgili Kişi Cep Telefon Numarası'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='related_person_title1',
            field=models.CharField(max_length=100, null=True, verbose_name='1.İlgili Ünvanı'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='related_person_title2',
            field=models.CharField(max_length=100, null=True, verbose_name='2.İlgili Ünvanı'),
        ),
    ]
