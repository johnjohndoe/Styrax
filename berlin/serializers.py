#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from . import models


class BerlinStreetTreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BerlinStreetTrees
