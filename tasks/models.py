from typing import Any
from django.db import models
from django.utils import timezone
from projects.models import Projects
from agent.models import Agent
from stage.models import StageTasks


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False,null=False)
    projects = models.ForeignKey(Projects, on_delete=models.PROTECT,related_name='task_project',blank=True)
    type = models.CharField(max_length=100,blank=False, null=False)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT,related_name='agent',blank=True)
    start_date = models.DateTimeField(blank=False,null=False)
    end_date = models.DateTimeField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    stage = models.ForeignKey(StageTasks,on_delete=models.PROTECT,related_name='task_stage',null=True)
    
    def __str__(self):
        return self.name
    
    def status(self):
        current_date = timezone.now()
        
        if self.start_date > current_date:
            return "Pendente"
        elif self.end_date < current_date:
            return "Atrasada"
        else:
            return "No Prazo"