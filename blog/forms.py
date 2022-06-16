from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Gives the option to add a comment to the bottom of a Blog Post, 
    but only for logged in users.
    """
    content = forms.CharField(widget=forms.Textarea(), label='')
    class Meta:
        model = Comment
        fields = [ 'content',]
    
    class Media:
        css = {
            'all': ('form.css',)
        }

