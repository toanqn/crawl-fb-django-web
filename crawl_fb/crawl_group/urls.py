from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.crawl_group, name='crawl_group'),
]