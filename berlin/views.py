#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . import geoutils
from . import models
from . import serializers


class BerlinStreetTreeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BerlinStreetTrees properties to be viewed.
    """
    queryset = models.BerlinStreetTrees.objects.all()
    serializer_class = serializers.BerlinStreetTreeSerializer
    pagination_class = PageNumberPagination


class DistanceView(viewsets.ViewSet):

    """
    API endpoint which returns the distance between two trees
    """
    def list(self, request, format=None):
        tree1 = request.query_params.get('tree1', None)
        tree2 = request.query_params.get('tree2', None)
        distance = geoutils.distance_between_trees(tree1, tree2)
        distance_hash = {'distance': distance}
        return Response(distance_hash, status=status.HTTP_200_OK)
