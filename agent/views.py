from django.shortcuts import render
from agent.models import Agent
from django.views.generic import ListView


class AgentListView(ListView):
    model = Agent
    template_name = "agent.html"
    context_object_name = 'agent'
