from django.db import models

class Staff(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    position=models.CharField(max_length=100)
    hire_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

