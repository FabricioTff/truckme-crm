from django.db import models


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=False,null=False)
    sector = models.CharField(max_length=50,blank=False,null=False)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.name