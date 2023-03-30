import os
from .common import *

SECRET_KEY = '&!he_zsd!)*oz+m0c7^$l58ra@e!+i9*rll9m@a-lc#t8rddfb'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tzfdapi',
        'HOST': 'mysql',
        'USER': 'root',
        'PASSWORD': 'abcd1234'
    },
    'mis': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': os.environ['ORACLE_SID'],
        'USER': os.environ['ORACLE_USER'],
        'PASSWORD': os.environ['ORACLE_PASSWORD'],
        'HOST': os.environ['ORACLE_HOST'],
        'PORT': os.environ['ORACLE_PORT']
    }
}
