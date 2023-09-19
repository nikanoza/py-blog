from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title