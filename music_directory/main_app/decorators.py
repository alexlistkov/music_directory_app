#This decorator checks user's ownership to the object.
#It means other users will not be able to do smth with objects via URLs.
#If somebody try to change or delete object he will get the '404' error.

from django.http import Http404
from .models import Music

def user_is_owner(function):
    def wrap(request, *args, **kwargs):
        music = Music.objects.get(id = kwargs['music_id'])
        if request.user.id == music.user_id:
            return function(request, *args, **kwargs)
        else:
            raise Http404('Object does not exist')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap