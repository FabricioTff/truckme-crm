from django.db import models

# Create your models here.
class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    birth_date = models.DateField(blank=True, null=True)
    rg = models.IntegerField(blank=True,null=True)
    uf_expedition = models.CharField(max_length=5,blank=True,null=True)
    cpf = models.IntegerField(blank=True,null=True)
    cnpj = models.IntegerField(blank=True,null=True)
    telefone = models.IntegerField(blank=True,null=True)
    celular = models.IntegerField(blank=True,null=True)
    emergency_phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    work_station = models.CharField(max_length=20,blank=True, null=True)
    address = models.CharField(max_length=150,blank=True,null=True)
    district = models.CharField(max_length=50,blank=True,null=True)
    zip_code = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    