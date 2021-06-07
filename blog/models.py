from django.db import models

# Create your models here.

class Profile(models.Model):
    title=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to='public/')
    creation=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
