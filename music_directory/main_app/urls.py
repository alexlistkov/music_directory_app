from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^post_url/$', views.post_music, name = 'post_music'),
    url(r'^user/(\w+)/$', views.profile, name = 'profile'),
    url(r'^login/$', views.login_view, name = 'login'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^([0-9]+)/del/$', views.del_music, name = 'del_music'),
    url(r'^add_to_fav/([0-9]+)/$', views.add_to_fav, name = 'add_to_fav'),
]