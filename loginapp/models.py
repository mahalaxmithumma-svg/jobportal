from django.db import models 
from django.contrib.auth.models import User






# Create your models here.
class Login(models.Model):
   username=models.CharField(max_length=100)
   email=models.EmailField()
   password=models.CharField(max_length=100)

class Register(models.Model):
   username=models.CharField(max_length=100,unique=True)
   FullName=models.CharField(max_length=100)
   email=models.EmailField()
   password=models.CharField(max_length=15)
   confirmpassword=models.CharField(max_length=15)
   mobileNo=models.CharField(max_length=15)
   
class Postjob(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary =models.IntegerField()
    job_type = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Adminregister(models.Model):
     name=models.CharField(max_length=100)
     email=models.EmailField()
     password=models.CharField(max_length=15)
     confirmpassword=models.CharField(max_length=15)


class AdminLogin(models.Model):

   email=models.EmailField()
   password=models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=100)
from django.db import models

class Userdetails(models.Model):
    
     job = models.ForeignKey(Postjob, on_delete=models.CASCADE)
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     position = models.CharField(max_length=50)
     company = models.CharField(max_length=100)
     designation  =models.CharField(max_length=100,default="TG")
     experience = models.CharField(max_length=50)
     state = models.TextField(max_length=100)
     city = models.CharField(max_length=100)
     phone = models.CharField(max_length=15)
     email = models.EmailField()
     address = models.TextField()
     dob = models.DateField()
     portfolio = models.URLField()
     resume = models.FileField(upload_to='resumes/')
     status=models.CharField(max_length=20, default="Pending")

class Profile(models.Model):
     user = models.ForeignKey(Register, on_delete=models.CASCADE)
     job = models.ForeignKey(Postjob, on_delete=models.CASCADE, null=True, blank=True)
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     position = models.CharField(max_length=50)
     company = models.CharField(max_length=100)
     designation  =models.CharField(max_length=100,default="TG")
     experience = models.CharField(max_length=50)
     state = models.TextField(max_length=100)
     city = models.CharField(max_length=100)
     phone = models.CharField(max_length=15)
     email = models.EmailField()
     address = models.TextField()
     dob = models.DateField()
     portfolio = models.URLField()
     resume = models.FileField(upload_to='resumes/')
     status=models.CharField(max_length=20, default="Pending")     
    

   
class Userdetailsreview(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, default="TG")
    experience = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField()
    portfolio = models.URLField()
    resume = models.FileField(upload_to='resumes/')
    status=models.CharField(max_length=20,default="success")


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(Postjob, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    experience = models.CharField(max_length=50,null=True, blank=True)
    resume = models.FileField(upload_to='resumes/')
    applied_on = models.DateTimeField(auto_now_add=True)
   

     
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]
        
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

   



