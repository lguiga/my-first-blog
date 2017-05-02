from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='detail'),
]