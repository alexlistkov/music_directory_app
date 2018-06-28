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
    url(r'^add_to_fav/$', views.add_to_fav, name = 'add_to_fav'),
    url(r'^favorites/$', views.favorites, name = 'favorites'),
    url(r'^order_by_year/$', views.order_by_year, name = 'order_by_year'),
    url(r'^order_by_artist/$', views.order_by_artist, name = 'order_by_artist'),
    url(r'^order_by_genre/$', views.order_by_genre, name = 'order_by_genre'),
    url(r'^order_by_album/$', views.order_by_album, name = 'order_by_album'),
    url(r'^order_by_title/$', views.order_by_title, name = 'order_by_title'),
    url(r'^year/([0-9]+)/$', views.filter_year, name = 'filter_year'),
    url(r'^artist/([-\w ]+)/$', views.filter_artist, name = 'filter_artist'),
    url(r'^genre/([-\w ]+)/$', views.filter_genre, name = 'filter_genre'),
    url(r'^album/([-\w ]+)/$', views.filter_album, name = 'filter_album'),
]