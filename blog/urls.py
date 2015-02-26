from django.conf.urls import patterns, include, url
from django.contrib import admin
import Blog.views
import profiles.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', profiles.views.login, name='login'),
    url(r'^logout', profiles.views.logout, name='logout'),
    url(r'^register', profiles.views.register, name='register'),

    url(r'^hello/', Blog.views.hello, name='hello'),
    url(r'^$', Blog.views.home, name='home'),
    url(r'^new_post', Blog.views.new_post, name='new_post'),
)
