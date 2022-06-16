from django.contrib import admin
from django import forms

from .models import BlogPost, Comment

from ckeditor.widgets import CKEditorWidget


class PostCommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class BlogPostAdminForm(forms.ModelForm):
    """
    Creates a custom form in the admin for adding blogposts
    """
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = ['title', 'sub_title', 'blog_author', 'content']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'date_posted', 'last_modified')

    inlines = [PostCommentInline]

