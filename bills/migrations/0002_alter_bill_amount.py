# Generated by Django 5.1 on 2025-03-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.FloatField(help_text='Total amount due for payment', verbose_name='Total Amount Owing (NGN)'),
        ),
    ]
