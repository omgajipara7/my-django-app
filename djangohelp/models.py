from django.db import models

class Member(models.Model):  # Change class name to singular form 'Member'
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.ImageField(null=True)  # Assuming this should be ImageField, not CharField
    joined_date = models.DateField(null=True)

def __str__(self):
    return f"{self.firstname} {self.lastname} {self.joined_date} "



#self


class Student(models.Model):
    name=models.CharField(max_length=20)
    enroll=models.IntegerField(null=True)
    branch=models.CharField(max_length=10)



#authentication

from django.db import models

class Auth(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    enroll = models.IntegerField(null=True)
    branch = models.CharField(max_length=10,null=True)


def __str__(self):
    return f" {self.username} {self.password}  {self.enroll} {self.branch}"