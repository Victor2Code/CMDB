#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-08
from django.urls import path

from API import views
from API.views import ServerView

urlpatterns = [
    path('test/', views.insert_date, name='test'),
    path('get_data/', views.get_data, name='get_data'),
    path('get_server/', views.get_server, name='get_server'),
    path('server/', ServerView.as_view(), name='server'),
]
