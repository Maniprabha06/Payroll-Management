# Generated by Django 4.2.1 on 2023-05-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_alter_employee_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MonthSalary', models.CharField(max_length=100)),
                ('WorkingDays', models.CharField(max_length=100)),
                ('BasicSalary', models.CharField(max_length=100)),
                ('HRASalary', models.CharField(max_length=100)),
                ('MediClaimSalary', models.CharField(max_length=100)),
                ('TASalary', models.CharField(max_length=200)),
                ('DASalary', models.CharField(max_length=200)),
                ('ReimbursementSalary', models.CharField(max_length=200)),
                ('CASalary', models.CharField(max_length=100)),
                ('DPFSalary', models.CharField(max_length=100)),
                ('DTAXSalary', models.CharField(max_length=100)),
                ('DeductionSalary', models.CharField(max_length=100)),
                ('Total', models.EmailField(max_length=100)),
            ],
        ),
    ]
