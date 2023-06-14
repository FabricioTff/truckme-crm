"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import TasksListView
from projects.views import ProjectsListView
from agent.views import AgentListView
from stage.views import StageListView
from tasks.views import TasksCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TasksListView.as_view(), name='tasks'),
    path('projects/',ProjectsListView.as_view(), name = 'projects'),
    path('agent/',AgentListView.as_view(),name='agent'),
    path('pipeline/',StageListView.as_view(),name='pipeline'),
    path('new_task/',TasksCreateView.as_view(), name='tasks_form')
]
