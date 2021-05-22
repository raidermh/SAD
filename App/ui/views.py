from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template import loader
from api import models
from . import forms


def logout_view(request, _):
    logout(request)
    return redirect(request.build_absolute_uri('/accounts/login/?next=/'))


@login_required
def projects(request):
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        form.save(commit=True)
    projects = models.Project.objects.order_by('-create_date')
    template = loader.get_template('projects.html')
    context = {
        'projects': projects,
        'form': forms.ProjectForm()
    }
    return HttpResponse(template.render(context, request))


@login_required
def releases(request):
    return render(request, 'releases.html')