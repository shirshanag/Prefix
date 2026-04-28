from django.db import models

# Create your models here.
class user_data(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=10)
    password=models.CharField(max_length=128)
    confirm_password=models.CharField(max_length=128)
    class Meta:
        db_table='user_data'
class contact_data(models.Model):
    Your_Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Message=models.CharField(max_length=500)
    class Meta:
        db_table='contact_data'
class  Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.IntegerField()
    old=models.IntegerField(null=True,blank=True)
    badge=models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    def __str__(self):
        return self.name


