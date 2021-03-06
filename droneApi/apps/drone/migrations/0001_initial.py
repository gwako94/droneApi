# Generated by Django 4.0 on 2021-12-27 10:56

from django.db import migrations, models
import droneApi.apps.drone.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('model', models.CharField(choices=[('Lightweight', 'Lightweight'), ('Middleweight', 'Middleweight'), ('Cruiserweight', 'Cruiserweight'), ('Heavyweight', 'Heavyweight')], default='Lightweight', max_length=50)),
                ('weight_limit', models.FloatField(validators=[droneApi.apps.drone.helpers.validate_weight])),
                ('battery_capacity', models.FloatField(validators=[droneApi.apps.drone.helpers.validate_percentage])),
                ('state', models.CharField(choices=[('idle', 'IDLE'), ('loading', 'LOADING'), ('loaded', 'LOADED'), ('delivering', 'DELIVERING'), ('delivered', 'DELIVERED'), ('returning', 'RETURNING')], default='idle', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
