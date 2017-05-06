from django.shortcuts import render
from django.http import HttpResponseRedirect
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
        form.save(commit = True)
    return HttpResponseRedirect('/')