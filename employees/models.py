from django.db import models
from django.contrib.auth.models import User


class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    reg_number = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    joined_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"