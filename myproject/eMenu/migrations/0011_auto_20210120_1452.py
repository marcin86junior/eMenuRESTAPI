# Generated by Django 3.0.7 on 2021-01-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0010_auto_20210120_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='add_time',
            field=models.DateTimeField(default='2021-01-20 13:52:30', verbose_name='Data dodania menu'),
        ),
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Opis menu'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='add_time',
            field=models.DateTimeField(default='2021-01-20 13:52:30', verbose_name='Data dodania przep.'),
        ),
    ]
