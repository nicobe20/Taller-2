from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models
from platform import architecture
# Create your models here.


class mlModels(models.Model):
    title= models.CharField(max_length = 50)
    descrition = models.CharField(max_length = 250) 
    architecture = models.FileField(upload_to ='mlmodels/')#json file , ni idea de esto porq esta aqui,, update ya se porq jaja
    weights = models.FileField(upload_to='mlmodels/') #h5 file esto si ni idea de porq esta aqui
    priority = models.PositiveSmallIntegerField(null=True)
