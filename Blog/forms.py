__author__ = 'erkoc'

from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        fields = ['title', 'content']
        model = Post
