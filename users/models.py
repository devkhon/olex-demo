from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import BaseModel

# ManyToMany
# ManyToOne
# OneToOne

class User(AbstractUser,BaseModel):
    photo = models.ImageField(upload_to='user/photos', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username