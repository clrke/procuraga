from django.conf.urls import patterns, include, url
from django.contrib import admin

import opportunities.views
import research.urls

urlpatterns = patterns('',
    # Examples:
    url(r'^$', opportunities.views.home, name='home'),

    url(r'^research/', include(research.urls)),

    url(r'^api/awards$', opportunities.views.awards, name='awards'),
    url(r'^api/bids$', opportunities.views.bids, name='bids'),
    url(r'^api/pperunit$',opportunities.views.pperunit, name='pperunit'),

    url(r'^api/supplier$',opportunities.views.supplier, name='supplier'),

    url(r'^admin/', include(admin.site.urls)),
)
