from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls import patterns

from .views import slack_cli

urlpatterns = patterns('',
        url(r'(?P<command>\w+[^/])/', slack_cli, name='slack_cli')
        )
