# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

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


    #add bank action form
    url(r'^(?P<user_id>\d+)/addbank/addbankaction/$', views.addbankaction,
        name='addbankaction'),


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




    #api v1.0

    #find user function
    url(r'^v1/finduser/$', csrf_exempt(views.v1finduser),
        name='finduser'),

    #find item function
    url(r'^v1/finditem/$', csrf_exempt(views.v1finditem),
        name='finditem'),

    #list all function
    url(r'^v1/listall/$', csrf_exempt(views.v1listall),
        name='listall'),

    #purchase an item
    url(r'^v1/purchase/$', csrf_exempt(views.v1purchase),
        name='v1purchase')
)
