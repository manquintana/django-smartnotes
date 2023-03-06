from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}), #In case you use bootstrap!
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'text': 'Write your thoughts here'
        }
    ''' Usar model forms nos permite validar facilmente lo que se carga en el form, ejemplo:'''
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise forms.ValidationError('We only accept notes with the word Django in title')

