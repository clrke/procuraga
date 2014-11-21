from django.conf.urls import patterns, include, url
from django.contrib import admin

import opportunities.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', opportunities.views.home, name='home'),
    url(r'^api/activities$', opportunities.views.activities, name='activities'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
