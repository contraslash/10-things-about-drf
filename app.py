#!/usr/bin/env python
import sys


from django.core.management import execute_from_command_line
from django.conf import settings
from django.urls import path
from django.views import generic
from django.http import response


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
# print(os.path.dirname(os.path.abspath(__file__)))
# print(sys.modules)
settings.configure(
    DEBUG=True,
    SECRET_KEY='A-random-secret-key!',
    ROOT_URLCONF=sys.modules[__name__],
    DATABASES=DATABASES,
    INSTALLED_APPS=['minimal_app']
)


class HelloWord(generic.View):

    def get(self, request):
        return response.HttpResponse("Hello World")


urlpatterns = [
    path('', HelloWord.as_view())
]

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
