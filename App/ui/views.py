from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def logout_view(request, _):
    logout(request)
    return redirect(request.build_absolute_uri('/accounts/login/?next=/'))


@login_required
def projects(request):
    return render(request, 'projects.html')


@login_required
def releases(request):
    return render(request, 'releases.html')