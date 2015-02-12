from django.test import TestCase
from blog.models import Post
from django.db.models import Model
from datetime import datetime, tzinfo


class PostTestCase(TestCase):
    
    def test_post_content(self):
        post = Post(
            title="Test Title",
            content_markdown="# Test #"
        )
        self.assertNotEqual(post.title, "")
        self.assertRegex(post.content_markdown, "#.*#")
        post.save()
        self.assertRegex(post.content_markup, "\<h1\>.*\<\/h1\>")
