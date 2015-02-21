from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
