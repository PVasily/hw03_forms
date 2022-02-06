from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import CD, GENRE_CHOICES


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):

        fields = ('first_name', 'last_name', 'username', 'email')

class ExchangeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=40)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    price = forms.DecimalField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)
    
    def clean_artist(self):
        artist = self.cleaned_data['artist']
        if CD.objects.filter(artist=artist).exists() == False:
            raise forms.ValidationError('Ваш диск не подходит для обмена')
        return artist
