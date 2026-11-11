from django.http import HttpResponse
from django.shortcuts import render
from .models import Project


def home(request):
    return HttpResponse(
        "Welcome to the Student Project Management System"
    )


def project_list(request):
    projects = Project.objects.all()

    return render(
        request,
        'projects/project_list.html',
        {'projects': projects}
    )