# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from newzuul import views

urlpatters = patterns('',

    url(r'^$', views.index, name='index'),

    url(r'^(?P<user_id>\d+/)/availability/$', views.availability, name='availability'),

    url(r'^(?P<user_id>\d+/)/profile/$', views.profile, name='profile'),

    url(r'^(?P<user_id>\d+/)/admin/$', views.admin, name='admin'),


    url(r'^(?P<user_id>\d+/)/available_shifts/$', views.available_shift,
        name='available_shifts'),
    )
