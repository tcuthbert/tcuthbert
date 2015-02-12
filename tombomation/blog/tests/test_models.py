from django.test import TestCase
from django.db.models import Model
from blog.models import Post, Category


class PostTestCase(TestCase):
    def setUp(self):
        post = Post.objects.create(title="Test", content_markdown="# Test Markdown #")
        categories = [u"foo", u"bar", u"test"]
        for cat in categories:
            cat = Category(title=cat)
            post.categories.add(cat)
        # for cat in categories:
        #     cat = Category.objects.create(title=cat)
            # post.categories.add(cat)

    def test_post_content(self):
        post = Post.objects.get(title="Test")
        self.assertNotEqual(post.title, "")
        self.assertRegex(post.content_markdown, "#.*#")
        self.assertRegex(post.content_markup, "\<h1\>.*\<\/h1\>")

    # def test_category(self):
