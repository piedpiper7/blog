from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^article/(?P<article_id>[0-9]+)/$',views.page,name='page'),
    url(r'^text/(?P<article_id>[0-9]+)/$',views.write,name='text'),
    url(r'^write/$',views.write_action,name='write_action'),
]