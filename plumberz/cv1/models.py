from django.db import models

# Create your models here.    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
class Music(models.Model):
    name = models.CharField(max_length=80)
    singer_name = models.CharField(max_length=130)
    image = models.ImageField(upload_to='static/images/')
    view = models.CharField(max_length=10, default='0')
    music_file = models.FileField(upload_to='static/music/', null=True, blank=True)
    

    def __str__(self):
        return self.name

