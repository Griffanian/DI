# Generated by Django 4.2 on 2023-04-27 12:06

from django.db import migrations,models
# from ..models import Rental

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [migrations.AlterField(
    model_name='Rental',
    name='return_date',
    field=models.DateField(null=True, blank=True)
)
    ]
