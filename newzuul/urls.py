# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from newzuul import views

urlpatterns = patterns('',
    #index, displays everyones name and bank balance
    url(r'^$', views.index, name='index'),

    #a purchase page, will display optoins for user to purchase
    url(r'^(?P<user_id>\d+)/purchase/$', views.purchaselist,
         name='purchaselist'),

    #purchase one item, for one user
    url(r'^(?P<user_id>\d+)/purchase/purchaseaction/$', views.purchaseaction,
        name='purchaseaction'),
)