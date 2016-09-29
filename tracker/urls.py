from django.conf.urls import url

from . import views

app_name = 'stories'
urlpatterns = [
    # ex: /stories/
    url(r'^$', views.index, name='index'),
    url(r'^evaluate$', views.evaluate, name='evaluate')
]
