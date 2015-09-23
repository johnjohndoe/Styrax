#!/usr/bin/env python
# -*- coding: utf-8 -*-

from styrax.settings_global import *


SECRET_KEY = 'not-a-secret-key'

DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
    }
}
