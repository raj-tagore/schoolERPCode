from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=500)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    phone = PhoneNumberField(_("Phone number"), blank=True)
    whatsapp = PhoneNumberField(_("Whatsapp number"), blank=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)
    phone = PhoneNumberField(_("Phone number"), blank=True)
    whatsapp = PhoneNumberField(_("Whatsapp number"), blank=True)
    
    def __str__(self):
        return self.username
    
class Student(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)
    phone = PhoneNumberField(_("Phone number"), blank=True)
    whatsapp = PhoneNumberField(_("Whatsapp number"), blank=True)
    standard = models.CharField(max_length=50)

    def __str__(self):
        return self.username
