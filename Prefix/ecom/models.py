from django.db import models

# Create your models here.
class user_data(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=10)
    password=models.CharField()
    confirm_password=models.CharField()
    class Meta:
        db_table='user_data'

