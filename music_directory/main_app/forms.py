from django import forms
from .models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'artist', 'genre', 'album', 'year', 'cover']

class LoginForm(forms.Form):
    username = forms.CharField(label = 'User Name', max_length = 64)
    password = forms.CharField(widget = forms.PasswordInput())