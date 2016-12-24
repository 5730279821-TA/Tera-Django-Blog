from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^orderbycontent', views.order_content, name='order_content'),
    url(r'^orderbyworkspace', views.order_workspace, name='order_workspace'),
    url(r'^about', views.about, name='about'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
     url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]