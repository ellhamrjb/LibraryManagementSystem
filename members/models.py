from django.db import models

class Role(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Member(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15,blank=True)
    membership_date=models.DateField(auto_now_add=True)
    role=models.ForeignKey(Role,on_delete=models.SET_NULL,null=True,blank=True,related_name='members')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
