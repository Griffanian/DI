# Generated by Django 4.2 on 2023-04-30 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 30, 9, 5, 19, 180275, tzinfo=datetime.timezone.utc)),
        ),
    ]
