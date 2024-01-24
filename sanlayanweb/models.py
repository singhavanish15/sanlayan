from django.db import models

# Create your models here.

class gallery1 (models.Model):
    gallery_typename = models.CharField(max_length=30)
    typename_bgpic = models.ImageField(upload_to="static/gallerypic")

    def __str__(self):
        return self.gallery_typename
    
class person(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13 ,default=False, null=True)
    email = models.EmailField()
    messagge = models.TextField()