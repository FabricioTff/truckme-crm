from django.shortcuts import render
from tasks.models import Tasks, StageTasks
from tasks.forms import TasksModelForm
from django.views.generic import CreateView,ListView,DetailView,UpdateView

class TasksListView(ListView):
    model = Tasks
    template_name = 'tasks.html'
    context_object_name = 'tasks'
    
class TasksCreateView(CreateView):
    model = Tasks
    form_class = TasksModelForm
    template_name = 'tasks_forms.html'
    success_url = '/tasks/'
    
    
    
    
    

    
