from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name








#email


from django.db import models





class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.name


