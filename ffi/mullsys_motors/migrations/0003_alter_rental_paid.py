# Generated by Django 4.1.3 on 2023-05-20 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mullsys_motors', '0002_rename_investment_rental'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='paid',
            field=models.CharField(max_length=20),
        ),
    ]
