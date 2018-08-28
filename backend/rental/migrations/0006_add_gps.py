# Generated by Django 2.0.7 on 2018-08-27 15:29

from django.contrib.postgres.operations import CreateExtension
import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_add_more_building_type'),
    ]

    operations = [
        CreateExtension('postgis'),
        migrations.RemoveField(
            model_name='house',
            name='rough_gps',
        ),
        migrations.RemoveField(
            model_name='housets',
            name='rough_gps',
        ),
        migrations.AddField(
            model_name='house',
            name='rough_coordinate',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='housets',
            name='rough_coordinate',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
