from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Music
from .forms import MusicForm, LoginForm, MusicAdditionalForm

# Create your views here.

def index(request):
    musics = Music.objects.filter(user = request.user)
    form = MusicForm
    return render(request, 'index.html', { 'musics': musics, 'form': form })

def detail(request, music_id):
    if request.user.id == Music.objects.get(id = music_id).user_id:
        if request.method == 'POST':
            instance = Music.objects.get(id = music_id)
            form = MusicAdditionalForm(request.POST, instance = instance)
            form_n = MusicForm(request.POST, instance = instance)
            if form.is_valid():
                    music = form.save(commit = False)
                    music.user = request.user
                    music.save()
            elif form_n.is_valid():
                    music = form_n.save(commit = False)
                    music.user = request.user
                    music.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:   
            music = Music.objects.get(id = music_id)
            form = MusicAdditionalForm
            form_n = MusicForm
            return render(request, 'details.html', { 'music': music, 'form': form, 'form_n': form_n })
    else:
        raise Http404

def post_music(request):
    form = MusicForm(request.POST)
    if form.is_valid():
        music = form.save(commit = False)
        music.user = request.user
        music.save()
    return HttpResponseRedirect('/')

def del_music(request, music_id):
    if request.user.id == Music.objects.get(id = music_id).user_id:
        instance = Music.objects.get(id = music_id)
        instance.delete()
        return HttpResponseRedirect('/')
    else:
        raise Http404

def profile(request, username):
    user = User.objects.get(username = username)
    musics = Music.objects.filter(user = user)
    return render(request, 'profile.html', {'username': username, 'musics': musics})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    form = LoginForm()
                    return render(request, 'login.html', { 'form': form, 'error': 'The account has been disabled!' })
            else:
                form = LoginForm()
                return render(request, 'login.html', { 'form': form, 'error': 'The username and password were incorrect.' })
        else:
            form = LoginForm()
            return render(request, 'login.html', { 'form': form, 'error': 'TRY AGAIN' })
    else:
        form = LoginForm()
        return render(request, 'login.html', { 'form': form })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        else:
            form = UserCreationForm()
            error = 'TRY AGAIN'
            return render(request, 'registration.html', { 'form': form, 'error': error })
    else:
        form = UserCreationForm()
        return render(request, 'registration.html', { 'form': form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

#def add_to_fav(request):
    #if request.method == "POST":
        #music_id = request.POST.get('music_id', None)
        #if (music_id):
            #music = Music.objects.get(id = int(music_id))
            #if music is not None:
                #if music.favorites == False:
                    #music.favorites = True
                    #music.save()
                #else:
                    #music.favorites = False
                    #music.save()
    #return HttpResponseRedirect('/')

def add_to_fav(request):
    music_id = request.POST.get('music_id', None)

    favorites = False
    if (music_id):
        music = Music.objects.get(id = int(music_id))
        if music is not None:
            if music.favorites == favorites:
                favorites = True
                music.favorites = favorites
                music.save()
            else:
                music.favorites = favorites
                music.save()
    return HttpResponse(favorites)

def favorites(request):
    user = request.user
    musics = Music.objects.filter(favorites = True, user = user)
    return render(request, 'favorites.html', {'musics': musics})

def order_by_year(request):
    order = request.GET.get('order', 'desc')
    my_music = Music.objects.filter(user = request.user)
    if(order == 'desc'):
        musics = my_music.order_by('-year')
    elif(order == 'asc'):
        musics = my_music.order_by('year')
    return render(request, 'favorites.html', {'musics': musics, 'order': order})

def order_by_artist(request):
    order = request.GET.get('order', 'desc')
    my_music = Music.objects.filter(user = request.user)
    if(order == 'desc'):
        musics = my_music.order_by('-artist')
    elif(order == 'asc'):
        musics = my_music.order_by('artist')
    return render(request, 'favorites.html', {'musics': musics, 'order': order})

def order_by_genre(request):
    order = request.GET.get('order', 'desc')
    my_music = Music.objects.filter(user = request.user)
    if(order == 'desc'):
        musics = my_music.order_by('-genre')
    elif(order == 'asc'):
        musics = my_music.order_by('genre')
    return render(request, 'favorites.html', {'musics': musics, 'order': order})

def order_by_album(request):
    order = request.GET.get('order', 'desc')
    my_music = Music.objects.filter(user = request.user)
    if(order == 'desc'):
        musics = my_music.order_by('-album')
    elif(order == 'asc'):
        musics = my_music.order_by('album')
    return render(request, 'favorites.html', {'musics': musics, 'order': order})

def order_by_title(request):
    order = request.GET.get('order', 'desc')
    my_music = Music.objects.filter(user = request.user)
    if(order == 'desc'):
        musics = my_music.order_by('-title')
    elif(order == 'asc'):
        musics = my_music.order_by('title')
    return render(request, 'favorites.html', {'musics': musics, 'order': order})

def filter_year(request, year):
    musics = Music.objects.filter(user = request.user, year = year)
    return render(request, 'filter.html', {'musics': musics})
    
def filter_artist(request, artist):
    musics = Music.objects.filter(user = request.user, artist = artist)
    return render(request, 'filter.html', {'musics': musics})

def filter_genre(request, genre):
    musics = Music.objects.filter(user = request.user, genre = genre)
    return render(request, 'filter.html', {'musics': musics})

def filter_album(request, album):
    musics = Music.objects.filter(user = request.user, album = album)
    return render(request, 'filter.html', {'musics': musics})