# Generated by Django 3.0.7 on 2021-01-20 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0005_auto_20210120_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static/', verbose_name='Obrazek'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dish',
            name='add_time',
            field=models.DateTimeField(default='2021-01-20 07:37:35', verbose_name='Data dodania przep.'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Opis dania'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_wege',
            field=models.CharField(max_length=50, verbose_name='Wegetariańskie'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nazwa dania'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='preparation_time',
            field=models.CharField(max_length=50, verbose_name='Przygotowanie (min)'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.CharField(max_length=50, verbose_name='Cena (zł)'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data zmiany przepisu'),
        ),
    ]
