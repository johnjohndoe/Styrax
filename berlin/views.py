#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from . import models
from . import serializers


class BerlinStreetTreeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows BerlinStreetTrees properties to be viewed.
    """
    queryset = models.BerlinStreetTrees.objects.all()
    serializer_class = serializers.BerlinStreetTreeSerializer
    pagination_class = PageNumberPagination
