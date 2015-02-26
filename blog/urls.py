from django.conf.urls import patterns, include, url
from blog.views import BlogView, PostItemView, DateArchiveBlogView, CategoryListView

urlpatterns = patterns('',
    url('archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', DateArchiveBlogView.as_view(date_field="date_publish"), name="blog-date-archive"),
    url('archive/(?P<slug>[-\w]+)/$', CategoryListView.as_view(), name="blog-category-archive"),
    url('(?P<slug>[-\w]+)/$', PostItemView.as_view(), name="blog-post-item"),
    url('^$', BlogView.as_view(), name="blog-post-index"),
)
