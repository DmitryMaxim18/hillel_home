import re
from django import forms
from core.models import Songs
from django.core.exceptions import ValidationError


class AddSongForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = '__all__'


class EditSongForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = ['name', 'duration', 'artist']






