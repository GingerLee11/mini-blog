from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Author(models.Model):
    """
    Defines the author of the blog.
    #TODO: Set this so that the author is automatically set
    to the logged in user. Also, restrict blog posting to logged in users only.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_born = models.DateField(help_text="Please enter in the date you were born.", null=True)
    short_bio = models.TextField(help_text="In a few words, describe yourself.", max_length=10000, null=True)

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BlogPost(models.Model):
    """
    Blog model describes the attributes of the blog posts
    and the relationships between the blogs and the comments and authors.
    """
    title = models.CharField(verbose_name="Blog Post Title", max_length=200, help_text="Please type in the title of this blog post")
    sub_title = models.CharField(verbose_name="Sub heading for the blog post", max_length=400, help_text="Enter a descriptive subheading, so that readers can have a better idea what the blog post is about.", blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True) # TODO: See how well this implementation works
    last_modified = models.DateField(auto_now=True)
    
    # TODO: Add a viewed attribute that increments anytime someone views the blog post

    blog_author = models.ManyToManyField(Author)
    content = models.TextField(max_length=1000000, help_text="Enter in the content for the blog post.")
    
    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Defines the comments that can be written about a blog post.
    """
    comment_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=1000, help_text="Please write a concise comment about the blog post.", blank=True)

    class Meta:
        ordering = ['last_modified']

    def __str__(self):
        return f"{self.comment_author}: {self.last_modified}"


class Hit(models.Model):
    """
    Generic hit model counts the number
    of views a certain page or object gets.
    """
    date = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()