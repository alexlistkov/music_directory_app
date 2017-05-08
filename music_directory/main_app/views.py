from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Music
from .forms import MusicForm, LoginForm, MusicAdditionalForm

# Create your views here.

def index(request):
    musics = Music.objects.all()
    form = MusicForm
    return render(request, 'index.html', { 'musics': musics, 'form': form })

def detail(request, music_id):
    if request.method == 'POST':
        instance = Music.objects.get(id = music_id)
        form = MusicAdditionalForm(request.POST, instance = instance)
        if form.is_valid():
                music = form.save(commit = False)
                music.user = request.user
                music.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:   
        music = Music.objects.get(id = music_id)
        form = MusicAdditionalForm
        return render(request, 'details.html', { 'music': music, 'form': form })

def post_music(request):
    form = MusicForm(request.POST)
    if form.is_valid():
        music = form.save(commit = False)
        music.user = request.user
        music.save()
    return HttpResponseRedirect('/')

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