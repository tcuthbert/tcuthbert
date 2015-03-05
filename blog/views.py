from django.views.generic import TemplateView, ArchiveIndexView, DetailView, ListView, MonthArchiveView, YearArchiveView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, Http404
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
        try:
            post = self.get_object()
            context["archive_dates"] = Post.objects.datetimes('date_publish', 'month', order='DESC')
            context["categories"] = Category.objects.filter(post__id=post.id)
        except Post.DoesNotExist:
            raise Http404("No Post matches the given query.")
        return context


class DateArchiveBlogView(MonthArchiveView):
    template_name = "blog/post/date_archive.html"
    model = Post
    context_object_name = "posts"

    def get_context_data(self, *args, **kwargs):
        context = super(DateArchiveBlogView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        archive_dates = Post.objects.datetimes('date_publish', 'month', order='DESC')
        categories = Category.objects.all()
        context["archive_dates"] = archive_dates
        context["categories"] = categories
        post_queryset = context["posts"]
        paginator = Paginator(post_queryset, 10)
        
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context["posts"] = posts
        return context

class CategoryDetailView(BlogView):
    template_name = "blog/post/category_archive.html"
    model = Category
    context_object_name = "category"
    
    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        post_queryset = Post.objects.filter(categories__slug__contains=kwargs['slug'])
        category = Category.objects.get(slug=kwargs['slug'])
        paginator = Paginator(post_queryset, 10)
        
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context["posts"] = posts
        context["category"] = category
        categories = Category.objects.all()
        context["categories"] = categories
        archive_dates = Post.objects.datetimes('date_publish', 'month', order='DESC')
        context["archive_dates"] = archive_dates
        return context
