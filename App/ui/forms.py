from django import forms
from django.forms import widgets
from api import models


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ('name', 'author', 'state', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows':3})
        }
        labels = {
            'name': 'Название',
            'author': 'Автор',
            'state': 'Состояние',
            'description': 'Описание'
        }


class RequirementForm(forms.ModelForm):
    class Meta:
        model = models.Requirement
        fields = ('name', 'type', 'author', 'status', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows':5,'cols':30})
        }
        labels = {
            'name': 'Название',
            'type': 'Тип',
            'author': 'Автор',
            'status': 'Статус',
            'description': 'Описание'
        }