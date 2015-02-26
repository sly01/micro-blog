__author__ = 'erkoc'

from django import forms
from Blog.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        fields = ['title', 'content']
        model = Post