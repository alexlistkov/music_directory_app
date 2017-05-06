from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Music
from .forms import MusicForm

# Create your views here.

def index(request):
    musics = Music.objects.all()
    form = MusicForm
    return render(request, 'index.html', { 'musics': musics, 'form': form })

def detail(request, music_id):
    music = Music.objects.get(id = music_id)
    return render(request, 'details.html', { 'music': music })

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