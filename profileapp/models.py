from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Personaldetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200,null=True, blank=True)
    lastname = models.CharField(max_length=200,null=True, blank=True)
    dob=models.CharField(max_length=200,null=True, blank=True)
    sex=models.CharField(max_length=200,null=True, blank=True)
    relation=models.CharField(max_length=200,null=True, blank=True)
    address=models.CharField(max_length=400,null=True, blank=True)
    place=models.CharField(max_length=200,null=True, blank=True)
    email = models.CharField(max_length=200,null=True, blank=True)
    phone=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Qualifications(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sslc=models.CharField(max_length=200,null=True, blank=True)
    sslcmark=models.IntegerField(null=True, blank=True)
    plustwo=models.CharField(max_length=200,null=True, blank=True)
    plustwomark=models.IntegerField(null=True, blank=True)
    degree=models.CharField(max_length=200,null=True, blank=True)
    degreemark=models.IntegerField(null=True, blank=True)
    pg=models.CharField(max_length=200,null=True, blank=True)
    pgmark=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
class Experience(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience1 = models.CharField(max_length=900,null=True, blank=True)
    experience2 = models.CharField(max_length=900,null=True, blank=True)
    experience3 = models.CharField(max_length=900,null=True, blank=True)
    experience4 = models.CharField(max_length=900,null=True, blank=True)


    def __str__(self):
        return self.user.username
class Skills(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skill1 = models.CharField(max_length=400,null=True, blank=True)
    skill2 = models.CharField(max_length=400,null=True, blank=True)
    skill3 = models.CharField(max_length=400,null=True, blank=True)
    skill4 = models.CharField(max_length=400,null=True, blank=True)

    def __str__(self):
        return self.user.username
class Projects(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projectname=models.CharField(max_length=200,null=True, blank=True)
    image=models.ImageField(upload_to='project_media',null=True, blank=True)
    link=models.URLField(max_length=300,null=True, blank=True)

    def __str__(self):
        return self.user.username
