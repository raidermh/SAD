from django import forms
from django.forms import widgets
from api import models

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ('name', 'author', 'description', 'state')
        widgets = {
            'description': forms.Textarea()
        }
        labels = {
            'name': 'Название',
            'author': 'Автор',
            'description': 'Описание',
            'state': 'Состояние'
        }