from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from users.models import BlogUser

from datetime import datetime, timezone
from math import floor

class BlogPost(models.Model):
    """
    Blog model describes the attributes of the blog posts
    and the relationships between the blogs and the comments and Users.
    """
    title = models.CharField(verbose_name="Blog Post Title", max_length=200, help_text="Please type in the title of this blog post")
    sub_title = models.CharField(verbose_name="Sub heading for the blog post", max_length=400, help_text="Enter a descriptive subheading, so that readers can have a better idea what the blog post is about.", blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True) # TODO: See how well this implementation works
    last_modified = models.DateField(auto_now=True)
    
    # TODO: Add a viewed attribute that increments anytime someone views the blog post

    blog_author = models.ManyToManyField(BlogUser)
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
    comment_author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=1000, help_text="Please write a concise comment about the blog post.", blank=True)

    class Meta:
        ordering = ['last_modified']

    def __str__(self):
        return f"{self.comment_author}: {self.last_modified}"

    @property
    def time_since_comment(self):
        """
        Converts the last modified attribute into a timedelta
        A time since comment
        """
        time_since = datetime.now(timezone.utc).timestamp() - self.last_modified.timestamp()
        time_unit = 'seconds'
        time_string = ''

        # Amount of seconds in each time unit
        MINUTE = 60
        HOUR = 3600
        DAY = 86400
        WEEK = 604800
        MONTH = 2592000
        YEAR = 31536000

        # Will return the highest time possible
        # Convert to years
        if time_since > YEAR:
            if time_since > YEAR * 2:
                time_unit = 'years'
            else:
                time_unit = 'year'
            time_string = f"{floor(time_since / 31536000)} {time_unit}"
        # Convert to months
        if time_since > MONTH:
            if time_since > MONTH * 2:
                time_unit = 'months'
            else:
                time_unit = 'month'
            time_string = f"{floor(time_since / 2592000)} {time_unit}"
        # Convert to weeks
        if time_since > WEEK:
            if time_since > WEEK * 2:
                time_unit = 'weeks'
            else:
                time_unit = 'week'
            time_string = f"{floor(time_since / 2592000)} {time_unit}"
        # Convert to days
        elif time_since > DAY:
            if time_since > DAY * 2:
                time_unit = 'days'
            else:
                time_unit = 'day'
            time_string = f"{floor(time_since / 86400)} {time_unit}"
        # Convert to hours
        elif time_since > HOUR:
            if time_since > HOUR * 2:
                time_unit = 'hours'
            else:
                time_unit = 'hour'
            time_string = f"{floor(time_since / 3600)} {time_unit}"
        # Convert to minutes
        elif time_since > MINUTE:
            if time_since > MINUTE * 2:
                time_unit = 'minutes'
            else:
                time_unit = 'minute'
            time_string = f"{floor(time_since / 60)} {time_unit}"
        # Convert to seconds
        else:
            time_string = f"{floor(time_since)} {time_unit}"
        # Return the time_string with the properly formatted time
        return time_string


class Hit(models.Model):
    """
    Generic hit model counts the number
    of views a certain page or object gets.
    """
    date = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
