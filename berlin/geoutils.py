#!/usr/bin/env python
# -*- coding: utf-8 -*-

from berlin.models import BerlinStreetTrees
from django.contrib.gis.measure import D


def distance_between_trees(tree1, tree2):
    tree1_pk = int(tree1)
    tree2_pk = int(tree2)
    if isinstance(tree1_pk, int) and isinstance(tree2_pk, int):
        real_tree1 = BerlinStreetTrees.objects.get(pk=tree1_pk)
        real_tree2 = BerlinStreetTrees.objects.get(pk=tree2_pk)
        return real_tree1.distance(real_tree2)
    raise ValueError("Parameters must be of type 'int'. "
                     "Check parameter: {0} and {1}".format(tree1, tree2))


def trees_within_distance(origin, distance):
    return BerlinStreetTrees.objects.filter(the_geom__distance_lte=(origin.the_geom, D(km=distance)))
