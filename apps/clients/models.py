from django.db import models

class Client(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New' 
        ACTIVE = 'active', 'Active' 
        INACTIVE = 'inactive', 'Inactive'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NEW)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"