from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from blog.models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', )
    search_fields = ('title', )
    fieldsets = (
        (
            None, 
            {
                'fields': ('title', 'slug',)
            }
        ),
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'content_markdown' : AdminPagedownWidget(),
        }
        exclude = ['content_markup',]

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date_publish')
    search_fields = ('title', 'content_markdown',)
    list_filter = ('categories',)
    fieldsets = (
        (
            None, 
            {
                'fields': ('title', 'slug', 'content_markdown', 'categories', 'date_publish',)
            }
        ),
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

