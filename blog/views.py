from django.views.generic import TemplateView, ArchiveIndexView, DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post
import calendar, datetime


class BlogView(TemplateView):
    template_name = "blog/post/index.html"
    blog_items = {}

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        self.blog_context_items()
        context["posts"] = self.blog_items["posts"]
        context["archive_dates"] = self.blog_items["archive_dates"]
        context["categories"] = self.blog_items["categories"]
        return context

    def blog_context_items(self):
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

        self.blog_items = {
                "posts": posts,
                "archive_dates": archive_dates,
                "categories": categories
            }

class PostItemView(DetailView):
    template_name = "blog/post/post_item.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, *args, **kwargs):
        context = super(PostItemView, self).get_context_data(**kwargs)
        post = self.get_object()
        context["archive_dates"] = Post.objects.datetimes('date_publish', 'month', order='DESC')
        context["categories"] = Category.objects.filter(post__id=post.id)
        return context

class DateArchiveBlogView(ArchiveIndexView):
    template_name = "blog/post/date_archive.html"
    model = Post

class CategoryListView(ListView):
    template_name = "blog/post/category_archive.html"
    model = Category
    context_object_name = "categories"
