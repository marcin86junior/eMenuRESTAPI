# Generated by Django 3.0.7 on 2021-01-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0008_auto_20210120_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='add_time',
            field=models.DateTimeField(default='2021-01-20 13:48:42', verbose_name='Data dodania menu'),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(blank=True, max_length=50, unique=True, verbose_name='Nazwa menu'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='add_time',
            field=models.DateTimeField(default='2021-01-20 13:48:42', verbose_name='Data dodania przep.'),
        ),
    ]
