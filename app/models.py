from django.db import models

# Create your models here.


class Admin(models.Model):
    Email = models.EmailField(
        max_length=25, default="Enter Email", unique=True)
    Password = models.CharField(max_length=25, default="Enter Password")
    Role = models.CharField(max_length=25, default="Enter Role")
    Otp = models.IntegerField(default=123456)
    Is_created = models.DateTimeField(auto_now_add=True)
    Is_verified = models.BooleanField(default=False)
    Is_active = models.BooleanField(default=False)


class Artist(models.Model):
    Artist = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=100, default="Firstname")
    Lastname = models.CharField(max_length=100, default="Lasttname")
    # Address = models.CharField(max_length=255, default="Address")
    Age = models.IntegerField(null=True)
    PhoneNumber = models.BigIntegerField(null=True)
    Gender = models.CharField(max_length=100, default="Gender")
    Loc = models.CharField(max_length=50, default="Select State")
    Designation = models.CharField(max_length=100, default="Who You Are")
    Intro = models.CharField(max_length=255, default="Introduce Yourself....")
    ProfilePic = models.ImageField(upload_to="artist/profile", default="abc")
    rate = models.FloatField(default=0.00)


class Customer(models.Model):
    Customer = models.ForeignKey(Admin, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=100, default="Firstname")
    Lastname = models.CharField(max_length=100, default="Lasttname")
    # Address = models.CharField(max_length=255, default="Address")
    Age = models.BigIntegerField(default=0)
    PhoneNumber = models.IntegerField(default=1234567890)
    Gender = models.CharField(max_length=100, default="Gender")
    Loc = models.CharField(max_length=50, default="Select State")
    ProfilePic = models.ImageField(default="customer/profile")

class BookArtistReq(models.Model):
    Cust = models.ForeignKey(Customer,on_delete=models.CASCADE)  
    Artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    Des = models.CharField(max_length=255,null=True)
    Status = models.CharField(max_length=100,default="Status")
