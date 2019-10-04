import os
import sys


from django.core.management import execute_from_command_line
from django.conf import settings
from django.urls import path

settings.configure(
    DEBUG=True,
    SECRET_KEY='A-random-secret-key!',
    ROOT_URLCONF=sys.modules[__name__],
)

urlpatterns = []

if __name__ == '__main__':
    execute_from_command_line(sys.argv)