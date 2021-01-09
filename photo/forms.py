from django import forms
from .models import PhotoSessions, client


class PhotosessionsForm(forms.ModelForm):
    class Meta:
        CHOICES = ('1', 'First',)
        model = PhotoSessions
        fields = '__all__'
        exclude = ('user', 'title', 'comment', 'client', 'status')
        widgets = {
#            'title': forms.TextInput(attrs={'class': 'form-control', }),
#            'comment': forms.TextInput(attrs={'class': 'form-control'}),
             'city': forms.Select(attrs={'class': 'form-control'}, choices=CHOICES),
             'boat': forms.Select(attrs={'class': 'form-control'}, )
   #     }
    #    labels = {
     #       'title': 'Заголовок'
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = '__all__'
        widgets = {
            'fio': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gorod': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'fio': 'ФИО',
            'telephone': 'Номер телефона',
            'email': 'Email',
            'gorod': 'Город',
        }
