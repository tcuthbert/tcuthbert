from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post
import calendar, datetime


class IndexView(TemplateView):
    template_name = "blog/post/index.html"
    feed_items = {}

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        self.feed()
        context["posts"] = self.feed_items["posts"]
        context["archive_dates"] = self.feed_items["archive_dates"]
        context["categories"] = self.feed_items["categories"]
        return context

    def feed(self):
        """Blog feed

        :param request: TODO
        :type request: django.http.request.HttpRequest
        :returns: TODO

        """

        archive_dates = Post.objects.datetimes('date_publish', 'month', order='DESC')
        categories = Category.objects.all()

        page = self.request.GET.get('page')
        post_queryset = Post.objects.all()
        paginator = Paginator(post_queryset, 5)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        self.feed_items = {
                "posts": posts,
                "archive_dates": archive_dates,
                "categories": categories
            }
        #return render (
            #self.render_to_response(self.template_name),
            #self.template_name,
            #{
                #"posts": posts,
                #"archive_dates": archive_dates,
                #"categories": categories
            #}
        #)

class PostItemView(TemplateView):
    template_name = "blog/post/post_item.html"

    #def __init__(self, *args, **kwargs):
        #super(PostItemView, self).__init__()

    def post_item(self, slug):
        """Render single post

        :param request: TODO
        :param slug: TODO
        :returns: TODO

        """
        
        post = get_object_or_404(Post, slug=slug)
        archive_dates = Post.objects.dates('date_publish', 'month', order="DESC")
        categories = Category.objects.all()
        return (
            self.render_to_response(self.template_name),
            self.template_name,
            {
                "posts": post,
                "archive_dates": archive_dates,
                "categories": categories
            }
        )

def date_archive(request, slug):
    """TODO: Docstring for date_archive.

    :param arg1: TODO
    :returns: TODO

    """
    pass
    
def category_archive(request, slug):
    """TODO: Docstring for category_archive.

    :param request: TODO
    :param slug: TODO
    :returns: TODO

    """
    pass
