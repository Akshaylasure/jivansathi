from django.db import models
from datetime import datetime


# chat/models.py
from django.db import models
from django.contrib.auth.models import User

class UserRelation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_relations"
    )
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friend_relations", default=None
    )
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.friend.username}"
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    
    
class Roles(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'roles'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

# Profile Model
class Profile(models.Model):
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=70)
    password = models.CharField(max_length=128)  # For hashed passwords
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name='profiles')
    mobile = models.CharField(max_length=15, blank=True, default='Not specified')
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Not specified')
    mother_tongue = models.CharField(max_length=50, default='Not specified')
    religion = models.CharField(max_length=50, default='Not specified')
    caste = models.CharField(max_length=100, default='Not specified')
    marriage_status = models.CharField(max_length=15, default='Not specified')
    height = models.CharField(max_length=10, default='Not specified')
    horoscope = models.CharField(max_length=50, default='Not specified')
    country = models.CharField(max_length=50, default='Not specified')
    state = models.CharField(max_length=50, default='Not specified')
    city = models.CharField(max_length=100, default='Not specified')
    degree = models.CharField(max_length=50, default='Not specified')
    employed_in = models.CharField(max_length=50, default='Not specified')
    occupation = models.CharField(max_length=50, default='Not specified')
    annual_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    career_about = models.TextField(default='')
    family_type = models.CharField(max_length=15, default='Not specified')
    father_occupation = models.CharField(max_length=50, default='Not specified')
    mother_occupation = models.CharField(max_length=50, default='Not specified')
    brother_count = models.IntegerField(default=0)
    family_living_in = models.CharField(max_length=100, default='Not specified')
    contact_address = models.TextField(default='Not specified')
    about_family = models.TextField(default='', blank=True)
    
    # New fields
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')  # Store the path to the profile picture
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['name']
        
        
        
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserRelation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_relations"
    )
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="friend_relations", default=None
    )
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.friend.username}"


class Messages(models.Model):
    description = models.TextField()
    sender_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sender"
    )
    receiver_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="receiver"
    )
    time = models.TimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ("timestamp",)
