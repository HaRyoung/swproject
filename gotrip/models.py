from django.db import models

# Create your models here.
class City(models.Model) :
    title = models.CharField(max_length= 200)
    img = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def res(self):
        return self.img
 
class Festa(models.Model):
    title =  models.CharField(max_length= 200)
    tag = models.CharField(max_length= 200)
    img = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title

    def cont(self):
        return self.content
