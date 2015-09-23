#!/usr/bin/env python
# -*- coding: utf-8 -*

from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'berlinstreettrees', views.BerlinStreetTreeViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
