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


class SpecificationForm(forms.ModelForm):
    requirements = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=models.Requirement.objects.all(),
        label='Требования',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(SpecificationForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['requirements'].initial = models.Requirement.objects.filter(specification_id=self.instance.id)
    
    def save(self, requirements):
        specification = super(SpecificationForm, self).save(commit=False)
        specification.save()
        specification.requirements.set(models.Requirement.objects.filter(pk__in=requirements))
        return specification

    class Meta:
        model = models.Specification
        fields = ('name', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows':3})
        }
        labels = {
            'name': 'Спецификация',
            'description': 'Описание'
        }


class ReleaseForm(forms.ModelForm):
    class Meta:
        model = models.Release
        fields = ('date', 'approver')
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'})
        }
        labels = {
            'date': 'Дата релиза',
            'approver': 'Согласующий'
        }