from django.db import models

# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")
    
    class Meta:
        verbose_name = "Abput Me"
        verbose_name_plural = "About Me"
        
    def __str__(self):
        return "About Me"
    
    
    
#Service Model
class Service(models.Model):
        name = models.CharField(max_length = 100, verbose_name = "Service name")
        description = models.TextField(verbose_name = "About service")
        
        def __str__(self):
            return self.name
        
#Recent Works
class RecentWork(models.Model):
    title = models.CharField(max_length = 100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")
    
    def __str__(self):
        return self.title
    
# Client model

class Client(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Client name")
    description = models.TextField(verbose_name = "Client Say")
    image = models.ImageField(upload_to="clients", default="default.png")
    
    def __str__(self):
        return self.name
    
    
    