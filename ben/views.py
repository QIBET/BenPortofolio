from django.http import request
from django.shortcuts import render
from .models import Projects

# Create your views here.

def index(request):

    title = "My Portofolio"
    projects = Projects.get_projects()

    context = {
    'title':title,
    'projects': projects
    }
    return render(request,'index.html', context)
