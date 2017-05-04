from django.shortcuts import render
from .models import Music

# Create your views here.

def index(request):
    musics = Music.objects.all()
    return render(request, 'index.html', {'musics': musics})