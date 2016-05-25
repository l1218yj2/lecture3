from django.conf.urls import patterns, url, include
from blog.views import detail, index

urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^(?P<pk>\d+)/', detail, name='detail'),
]
