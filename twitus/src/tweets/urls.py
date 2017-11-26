
from django.conf.urls import url
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^(?P<id>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
]
