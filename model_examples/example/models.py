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

# Replica actividad del primer y segundo video 'One To Many Relationships' y 'Query One To Many'.

class Language(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
# Finzalizacion de la actividad del primer y segundo video 'One To Many Relationships' y 'Query One To Many'.
    
# Replica actividad del tercer y cuarto video 'Many To Many Relationships' y 'Many To Many Query'.

class Movie(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
        
class Character(models.Model):
    name = models.CharField(max_length=10)
    movies = models.ManyToManyField(Movie)
    
    def __str__(self):
        return self.name
     
# Finzalizacion de la actividad del tercer y cuarto video 'Many To Many Relationships' y 'Many To Many Query'.
