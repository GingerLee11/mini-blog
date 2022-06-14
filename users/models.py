from django.db import models
from django.contrib.auth.models import AbstractUser


class BlogUser(AbstractUser):
    """
    BlogUser inherits from the default django User model
    Is very similar to the User model except that it adds
    a few more attributes such as a bio, date_born and more information.
    """
    date_born = models.DateField(help_text="Please enter in the date you were born.", null=True)
    short_bio = models.TextField(help_text="In a few words, describe yourself.", max_length=10000, null=True)
 
    
    def __str__(self):
        return f"{self.username}"