from django.contrib import admin

# Register your models here.

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'user']
    list_filter = ['title', 'content']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)