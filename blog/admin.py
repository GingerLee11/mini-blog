from django.contrib import admin

from .models import Author, BlogPost, Comment

class PostCommentInline(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'last_modified')

    inlines = [PostCommentInline]

admin.site.register(Author)
# admin.site.register(BlogPost)
# admin.site.register(Comment)