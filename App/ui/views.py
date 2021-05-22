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
def project(request, project_id):
    project = models.Project.objects.get(pk=project_id)
    if request.method == 'POST':
        if 'type' in request.POST:
            form = forms.RequirementForm(request.POST)
            requirement = form.save(commit=False)
            requirement.project_id = project_id
            requirement.save()
        else:
            form = forms.ProjectForm(request.POST, instance=project)
            form.save(commit=True)
    template = loader.get_template('project.html')
    context = {
        'project': project,
        'form': forms.ProjectForm(instance=project),
        'requirement_form': forms.RequirementForm()
    }
    return HttpResponse(template.render(context, request))


@login_required
def delete_project(request, project_id):
    project = models.Project.objects.get(pk=project_id)
    project.delete()
    return redirect(request.build_absolute_uri('/'))


@login_required
def requirement(request, requirement_id):
    requirement = models.Requirement.objects.get(pk=requirement_id)
    if request.method == 'POST':
        form = forms.RequirementForm(request.POST, instance=requirement)
        form.save(commit=True)
    template = loader.get_template('requirement.html')
    context = {
        'requirement': requirement,
        'form': forms.RequirementForm(instance=requirement)
    }
    return HttpResponse(template.render(context, request))


@login_required
def delete_requirement(request, requirement_id):
    requirement = models.Requirement.objects.get(pk=requirement_id)
    project_id = requirement.project_id
    requirement.delete()
    return redirect(request.build_absolute_uri('/project/' + str(project_id) + '/'))


@login_required
def releases(request):
    return render(request, 'releases.html')