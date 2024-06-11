from django.db import models

# Create your models here.

class Simple(models.Model):
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')
    
    def __str__(self):
        return self.url
        
class DateExample(models.Model):
    the_date = models.DateTimeField()
    
class NullExample(models.Model):
    col = models.CharField(max_length=10, blank=True, null=True)
    
# Inicio de replicar actividad del segundo Video 'Query One To Many'

class Language(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
# Finalización de replicar actividad del segundo Video 'Query One To Many'