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


class RequirementForm(forms.ModelForm):
    class Meta:
        model = models.Requirement
        fields = ('name', 'type', 'author', 'status', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows':5,'style':'vertical-align:middle;margin-top:0.5rem;'})
        }
        labels = {
            'name': 'Название',
            'type': 'Тип',
            'author': 'Автор',
            'status': 'Статус',
            'description': 'Описание'
        }