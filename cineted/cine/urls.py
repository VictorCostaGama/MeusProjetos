from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<filme_title>[\w ]+)/$', views.detalhes, name='detalhes'),
]