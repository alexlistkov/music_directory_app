from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^post_url/$', views.post_music, name = 'post_music'),
    url(r'^user/(\w+)/$', views.profile, name = 'profile'),
]