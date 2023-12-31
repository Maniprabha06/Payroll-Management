# Generated by Django 4.2 on 2023-05-19 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('MiddleName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('DOB', models.IntegerField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Mobile', models.IntegerField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Pincode', models.IntegerField(max_length=100)),
                ('Nationality', models.CharField(max_length=100)),
                ('UserName', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('ConfirmPass', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
            ],
        ),
    ]
