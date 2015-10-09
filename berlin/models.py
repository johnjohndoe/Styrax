#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.gis.db import models


class BerlinStreetTrees(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    the_geom = models.PointField(srid=25833, geography=True, blank=True, null=True)  # This field type is a guess.
    gml_id = models.CharField(max_length=254, blank=True, null=True)
    spatial_name = models.CharField(db_column='spatial_na', max_length=254, blank=True, null=True)
    spatial_alias = models.CharField(db_column='spatial_al', max_length=254, blank=True, null=True)
    spatial_type = models.CharField(db_column='spatial_ty', max_length=254, blank=True, null=True)
    location_number = models.CharField(db_column='standortnr', max_length=254, blank=True, null=True)
    identification_tag = models.CharField(db_column='kennzeich', max_length=254, blank=True, null=True)
    name_number = models.CharField(db_column='namenr', max_length=254, blank=True, null=True)
    species_german = models.CharField(db_column='art_dtsch', max_length=254, blank=True, null=True)
    species_botanical = models.CharField(db_column='art_bot', max_length=254, blank=True, null=True)
    genus = models.CharField(db_column='gattung', max_length=254, blank=True, null=True)
    alk_nr4st = models.CharField(db_column='alk_nr4st', max_length=254, blank=True, null=True)
    street_name = models.CharField(db_column='strname', max_length=254, blank=True, null=True)
    house_number = models.CharField(db_column='hausnr', max_length=254, blank=True, null=True)
    extension = models.CharField(db_column='zusatz', max_length=254, blank=True, null=True)
    year_of_planting = models.CharField(db_column='pflanzjahr', max_length=254, blank=True, null=True)
    age = models.CharField(db_column='standalter', max_length=254, blank=True, null=True)
    crown_diameter = models.CharField(db_column='kronedurch', max_length=254, blank=True, null=True)
    trunk_circumference = models.CharField(db_column='stammumfg', max_length=254, blank=True, null=True)
    tree_height = models.CharField(db_column='baumhoehe', max_length=254, blank=True, null=True)

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'strassenbaeume_berlin_mitte'

    def distance(self, other):
        if isinstance(other, BerlinStreetTrees):
            return self.the_geom.distance(other.the_geom)
        if isinstance(other, int):
            other_tree = BerlinStreetTrees.objects.get(pk=other)
            return self.the_geom.distance(other_tree.the_geom)
        raise ValueError("Parameter must be either of type 'BerlinStreetTrees' or of type 'int'. "
                         "Check parameter: {0}".format(other))

    # Returns the string representation of the model.
    def __str__(self):  # __unicode__ on Python 2
        return self.gml_id
