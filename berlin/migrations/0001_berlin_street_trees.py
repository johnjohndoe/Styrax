#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BerlinStreetTrees',
            fields=[
                ('ogc_fid', models.AutoField(serialize=False, primary_key=True)),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(blank=True, srid=25833, geography=True, null=True)),
                ('gml_id', models.CharField(blank=True, max_length=254, null=True)),
                ('spatial_name', models.CharField(blank=True, max_length=254, db_column='spatial_na', null=True)),
                ('spatial_alias', models.CharField(blank=True, max_length=254, db_column='spatial_al', null=True)),
                ('spatial_type', models.CharField(blank=True, max_length=254, db_column='spatial_ty', null=True)),
                ('location_number', models.CharField(blank=True, max_length=254, db_column='standortnr', null=True)),
                ('identification_tag', models.CharField(blank=True, max_length=254, db_column='kennzeich', null=True)),
                ('name_number', models.CharField(blank=True, max_length=254, db_column='namenr', null=True)),
                ('species_german', models.CharField(blank=True, max_length=254, db_column='art_dtsch', null=True)),
                ('species_botanical', models.CharField(blank=True, max_length=254, db_column='art_bot', null=True)),
                ('genus', models.CharField(blank=True, max_length=254, db_column='gattung', null=True)),
                ('alk_nr4st', models.CharField(blank=True, max_length=254, db_column='alk_nr4st', null=True)),
                ('street_name', models.CharField(blank=True, max_length=254, db_column='strname', null=True)),
                ('house_number', models.CharField(blank=True, max_length=254, db_column='hausnr', null=True)),
                ('extension', models.CharField(blank=True, max_length=254, db_column='zusatz', null=True)),
                ('year_of_planting', models.CharField(blank=True, max_length=254, db_column='pflanzjahr', null=True)),
                ('age', models.CharField(blank=True, max_length=254, db_column='standalter', null=True)),
                ('crown_diameter', models.CharField(blank=True, max_length=254, db_column='kronedurch', null=True)),
                ('trunk_circumference', models.CharField(blank=True, max_length=254, db_column='stammumfg', null=True)),
                ('tree_height', models.CharField(blank=True, max_length=254, db_column='baumhoehe', null=True)),
            ],
            options={
                'db_table': 'strassenbaeume_berlin_mitte',
                'managed': False,
            },
        ),
    ]
