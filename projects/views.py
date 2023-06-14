from django.shortcuts import render
from django.views.generic import ListView
from projects.models import Projects

class ProjectsListView(ListView):
    model = Projects
    template_name = 'projects.html'
    context_object_name = 'projects'
