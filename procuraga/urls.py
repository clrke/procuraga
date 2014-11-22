from django.conf.urls import patterns, include, url
from django.contrib import admin

import opportunities.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', opportunities.views.home, name='home'),
    url(r'^api/awards$', opportunities.views.awards, name='awards'),
    url(r'^api/bids$', opportunities.views.bids, name='bids'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/pperunit$',opportunities.views.pperunit, name='pperunit'),
    url(r'^admin/', include(admin.site.urls)),
)
