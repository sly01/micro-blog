__author__ = 'erkoc'

from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        fields = ['title', 'content']
        model = Post


class CommentForm(forms.ModelForm):

    class Meta:
        fields = ['content']
        model = Comment