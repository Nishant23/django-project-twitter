
from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetUpdateView.as_view(), name='delete'),
    url(r'^search/$', TweetListView.as_view(), name='list'),
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
]
