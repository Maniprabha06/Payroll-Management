# Generated by Django 4.2.1 on 2023-05-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0004_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Total',
            field=models.CharField(max_length=100),
        ),
    ]