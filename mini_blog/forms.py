from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout,  Div, Field

from users.models import BlogUser

class Row(Div):
    css_class = 'row'

class BlogUserCreationForm(UserCreationForm):
    """
    Create a custom user creation form using the bloguser model that I defined.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_id = 'id_blog_user_creation_form'
        # self.helper.form_class = 'blueForms'
        # self.helper.form_method = 'post'
        # self.helper.form_action = ''
        # self.helper.form_tag = False
        # self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(
                Field('username', wrapper_class='form-group col-md-6 mb-0'),
                Field('email', wrapper_class='form-group col-md-6 mb-0'),
            ),
            'password1',
            'password2',
            Row(
                Field('first_name', wrapper_class='form-group col-md-4 mb-0'),
                Field('last_name', wrapper_class='form-group col-md-4 mb-0'),
                Field('date_born', wrapper_class='form-group col-md-4 mb-0'),
            ),
            'short_bio',
            Submit('submit', 'Submit')
        )

    class Meta:
        model = BlogUser
        fields = ("username", 'email', 'password1', 'password2', 'first_name', 'last_name', 'date_born', 'short_bio')


