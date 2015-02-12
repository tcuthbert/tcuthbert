from django.db import models
from markdown import markdown

# Create your models here.
# Reference: http://www.yaconiello.com/blog/part-1-creating-blog-system-using-django-markdown/

class Category(models.Model):
    """Category Model"""
    title = models.CharField(
        verbose_name = (u'Title'),
        help_text = (u' '),
        max_length = 255
    )
    slug = models.SlugField(
        verbose_name = (u'Slug'),
        help_text = (u'Uri identifier.'),
        max_length = 255,
        unique = True
    )

    class Meta:
        app_label = (u'blog')
        verbose_name = (u"Category")
        verbose_name_plural = (u"Categories")
        ordering = ['title',]

    def __unicode__(self):
        return "%s" % (self.title, )


class Post(models.Model):
    """Post Model"""
    title = models.CharField(
        verbose_name = (u'Title'),
        help_text = (u' '),
        max_length = 255
    )
    slug = models.SlugField(
        verbose_name = (u'Slug'),
        help_text = (u'Uri identifier.'),
        max_length = 255,
        unique = True
    )
    content_markdown = models.TextField(
        verbose_name = (u'Content (Markdown)'),
        help_text = (u'')
    )
    content_markup = models.TextField(
        verbose_name = (u'Content (Markup)'),
        help_text = (u' ')
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name = (u'Categories'),
        help_text = (u' '),
        null = True,
        blank = True
    )
    date_publish = models.DateTimeField(
        verbose_name = (u'Publish Date'),
        help_text = (u' '),
        auto_now=True
    )

    class Meta:
        app_label = (u'blog')
        verbose_name = (u'Post')
        verbose_name_plural = (u'Posts')
        ordering = ['-date_publish']

    def save(self, *args, **kwargs):
        self.content_markup = markdown(self.content_markdown, ['codehilite'])
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % (self.title,)
