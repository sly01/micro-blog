from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'user']
    list_filter = ['title', 'content']


admin.site.register(Post, PostAdmin)