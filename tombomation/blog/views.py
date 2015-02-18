from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post
import calendar, datetime


class IndexView(TemplateView):
    template_name = "blog/post/index.html"

    #def __init__(self, *args, **kwargs):
        #super(IndexView, self).init(*args, **kwargs)

    def index(self):
        """Blog Index

        :param request: TODO
        :type request: django.http.request.HttpRequest
        :returns: TODO

        """

        archive_dates = Post.objects.dates('date_publish', 'month', order='DESC')
        categories = Category.objects.all()

        page = self.get('page')
        post_queryset = Post.objects.all()
        paginator = Paginator(post_queryset, 5)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render (
            self.render_to_response(self.template_name),
            self.template_name,
            {
                "posts": posts,
                "archive_dates": archive_dates,
                "categories": categories
            }
        )

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
                "posts": posts,
                "archive_dates": archive_dates,
                "categories": categories
            }
        )

def date_archive(request, slug):
    """TODO: Docstring for date_archive.

    :param arg1: TODO
    :returns: TODO

    """
    
def category_archive(request, slug):
    """TODO: Docstring for category_archive.

    :param request: TODO
    :param slug: TODO
    :returns: TODO

    """
    pass
