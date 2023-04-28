# Generated by Django 4.2 on 2023-04-27 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('real_cost', models.FloatField()),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.vehiclesize')),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='RentalRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_rate', models.FloatField()),
                ('vehicle_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.vehiclesize')),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.customer')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.vehicle')),
            ],
        ),
    ]
