from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.crawl_page, name='crawl_page')
]