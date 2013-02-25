from __future__ import absolute_import

from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns('',
    url(r'^mine/$',
        views.my_feeds,
        name='community-my-feeds'
    ),
    url(
        r'^(?P<feed_type_slug>[-\w]+)/$',
        views.feed_list,
        name="community-feed-list"
    ),
    url(
        r'^add/(?P<feed_type_slug>[-\w]+)/$',
        views.add_feed,
        name='community-add-feed'
    ),
    url(
        r'^edit/(?P<feed_id>\d+)/$',
        views.edit_feed,
        name='community-edit-feed'
    ),
    url(
        r'^delete/(?P<feed_id>\d+)/$',
        views.delete_feed,
        name='community-delete-feed'
    ),
)
