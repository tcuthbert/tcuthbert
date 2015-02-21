from django.conf.urls import patterns, include, url
#from django.views.generic.simple import direct_to_template
from blog.views import IndexView, PostItemView

urlpatterns = patterns('',
    url('^blog/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blog.views.post.date_archive', name="blog-date-archive"),
    url('^blog/archive/(?P<slug>[-\w]+)/$', 'blog.views.post.category_archive', name="blog-category-archive"),
    url('^blog/(?P<slug>[-\w]+)/$', PostItemView.as_view(), name="blog-post-item"),
    url('(^$|^blog/$)', IndexView.as_view(template_name="blog/post/index.html"))
)
