from django.conf.urls import patterns, include, url
from blog.views import BlogView, PostItemView, DateArchiveBlogView, CategoryBlogView

urlpatterns = patterns('',
    url('^blog/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', DateArchiveBlogView.as_view(), name="blog-date-archive"),
    url('^blog/archive/(?P<slug>[-\w]+)/$', CategoryBlogView.as_view(), name="blog-category-archive"),
    url('^blog/(?P<slug>[-\w]+)/$', PostItemView.as_view(), name="blog-post-item"),
    url('(^$|^blog/$)', BlogView.as_view(), name="blog-post-index")
)
