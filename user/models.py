from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    mobile=models.CharField(max_length=20)
    message=models.CharField(max_length=600)



def __str__(self):
    return self.email

class category(models.Model):
    cname=models.CharField(max_length= 30)
    cpic=models.ImageField(upload_to='static/category/',default="")
    cdate=models.DateField()

class gallery(models.Model):
    pdes=models.CharField(max_length=200)
    gpic=models.ImageField(upload_to='static/gallery',default="")
    gdate=models.DateField()

class notification(models.Model):
    name=models.CharField(max_length=200)
    rpic=models.ImageField(upload_to='static/recuiters',default="")
    rdate=models.DateField()

class courses(models.Model):
    cname=models.CharField(max_length=200)
    cpic=models.ImageField(upload_to='static/courses',default="")
    cdate = models.DateField()

    def __str__(self):
        return self.cname


class admission(models.Model):
    name=models.CharField(max_length=100)
    pcourse=models.ForeignKey(courses,on_delete=models.CASCADE)
    branch=models.CharField(max_length=80)
    cmpname=models.CharField(max_length=80)
    cmplogo=models.ImageField(upload_to='static/placement',default="")
    city=models.CharField(max_length=100)
    pyear=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    stupic=models.ImageField(upload_to='static/studentpic/',default="")
    pdate=models.DateField()

class faculty(models.Model):
    name=models.CharField(max_length=50)
    about=models.TextField(max_length=300)
    pic=models.ImageField(upload_to='static/gallery/', default="")






















