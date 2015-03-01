from django.conf.urls import patterns, include, url
from django.contrib import admin
import blog.views
import profiles.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', profiles.views.login, name='login'),
    url(r'^logout', profiles.views.logout, name='logout'),
    url(r'^register', profiles.views.register, name='register'),

    url(r'^hello/', blog.views.hello, name='hello'),
    url(r'^$', blog.views.home, name='home'),
    url(r'^new_post', blog.views.new_post, name='new_post'),
    url(r'^post/(?P<pk>[\d]+)$', blog.views.post_detail, name='post_detail'),
    url(r'^delete_post/(?P<pk>[\d]+)$', blog.views.delete_post, name='delete_post'),

    url(r'^new_comment/(?P<pk>[\d]+)$', blog.views.add_comment, name='new_comment'),
    url(r'^edit_post/(?P<pk>[\d]+)$', blog.views.edit_post, name='edit_post'),

)
