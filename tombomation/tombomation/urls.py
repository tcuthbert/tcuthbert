from django.conf.urls import patterns, include, url
from django.contrib import admin
from autofixture.autofixtures import autofixture
from tombomation.settings import DEBUG

if DEBUG == True:
    autofixture.autodiscover()

urlpatterns = patterns('',
    url('^blog/', include('blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
