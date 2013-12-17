#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from .views import (BlogPostList, BlogPostDetail, BlogList, BlogUsersList,
                    CategoryList)
from .conf import settings


urlpatterns = patterns(
    '',
    url(r'^{}/(?P<blog__slug>[\w\b-]+)/authors/?$'.format(
        settings.OPPS_BLOGS_CHANNEL),
        cache_page(settings.OPPS_CACHE_EXPIRE)(BlogUsersList.as_view()),
        name='blogusers-list',
        kwargs={'channel__long_slug': settings.OPPS_BLOGS_CHANNEL}),
    url(r'^{}/(?P<blog__slug>[\w\b-]+)/(?P<category_long_slug>[\w\b//-]+)/(?P<slug>[\w-]+)\.html$'.format(
        settings.OPPS_BLOGS_CHANNEL),
        cache_page(settings.OPPS_CACHE_EXPIRE)(BlogPostDetail.as_view()),
        name='blogpost-detail',
        kwargs={'channel__long_slug': settings.OPPS_BLOGS_CHANNEL, }),
    url(r'^{}/(?P<blog__slug>[\w\b-]+)/(?P<category_long_slug>[\w\b//-]+)?/$'.format(
        settings.OPPS_BLOGS_CHANNEL),
        cache_page(settings.OPPS_CACHE_EXPIRE)(CategoryList.as_view()),
        name='category-list',
        kwargs={'channel__long_slug': settings.OPPS_BLOGS_CHANNEL}),
    url(r'^{}/(?P<blog__slug>[\w\b-]+)?/$'.format(settings.OPPS_BLOGS_CHANNEL),
        cache_page(settings.OPPS_CACHE_EXPIRE)(BlogPostList.as_view()),
        name='blogpost-list',
        kwargs={'channel__long_slug': settings.OPPS_BLOGS_CHANNEL}),
    url(r'^{}/'.format(settings.OPPS_BLOGS_CHANNEL),
        cache_page(settings.OPPS_CACHE_EXPIRE)(BlogList.as_view()),
        name='blog-list',
        kwargs={'channel__long_slug': settings.OPPS_BLOGS_CHANNEL}),
)
