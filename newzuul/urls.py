# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from newzuul import views

urlpatterns = patterns('',
    #index, displays everyones name and bank balance
    url(r'^$', views.index, name='index'),

    #a purchase page, will display options for user to purchase
    url(r'^(?P<user_id>\d+)/purchase/$', views.purchaselist,
         name='purchaselist'),

    #purchase lots-o-items for one user
    url(r'^(?P<user_id>\d+)/purchase/purchaseaction/$', views.purchaseaction,
        name='purchaseaction'),



    #Add an item page
    url(r'^additem/$', views.additemform,
        name='additemform'),

    #Add an item action page
    url(r'^additemaction/$', views.additemaction,
        name='additemaction'),



    #Add a user page
    url(r'^adduser/$', views.adduserform,
        name='adduserform'),

    #Add a user page
    url(r'^adduseraction/$', views.adduseraction,
        name='adduseraction'),
)