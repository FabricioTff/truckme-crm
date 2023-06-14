from django.db import models

class StageTasks(models.Model):
    id = models.AutoField(primary_key=True)
    STAGES_CHOICES = [
        (1, "A Fazer"),
        (2, "Fazendo"),
        (3, "Em Aprovação"),
        (4, "Realizado"),
    ]
    stage = models.IntegerField(choices=STAGES_CHOICES)
    
    def __str__(self):
        return dict(self.STAGES_CHOICES)[self.stage]
    
    
class StageComercial(models.Model):
    id = models.AutoField(primary_key=True)
    STAGES_CHOICES = [
        (1, "Sem Contato"),
        (2, "Contato Feito"),
        (3, "Identificação de Interesse"),
        (4, "Apresentação"),
        (5, "Proposta Enviada"),
    ]
    
    stage = models.CharField(max_length=100,choices=STAGES_CHOICES)
    
    def __str__(self):
        return self.stage