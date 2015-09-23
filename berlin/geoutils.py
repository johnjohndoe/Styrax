#!/usr/bin/env python
# -*- coding: utf-8 -*-

from berlin import models
from django.contrib.gis.measure import D


def distance_between_trees(tree1, tree2):
    return tree1.distance(tree2)


def trees_within_distance(origin, distance):
    return models.BerlinStreetTrees.objects.filter(the_geom__distance_lte=(origin.the_geom, D(km=distance)))
