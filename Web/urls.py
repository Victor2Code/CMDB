#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-08


from django.urls import path

from Web import views

urlpatterns = [
    path('index/', views.index, name='index'),
]