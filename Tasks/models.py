from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class customUser(AbstractUser):
    isAdmin = models.BooleanField(default=False)
    profilePhoto = models.ImageField(upload_to='profile_photos', null=True, blank=True, default='profile_photos/default.jpg')

Priority = (
    ('high', 'high'),
    ('medium', 'medium'),
    ('low', 'low'),
)

Category = (
    ('Work', 'Work'),
    ('Personal', 'Personal'),
    ('Shopping', 'Shopping'),
    ('Health', 'Health'),
    ('Fiance', 'Fiance'),
    ('Other', 'Other'),
)

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=20, choices=Priority)
    category = models.CharField(max_length=20, choices=Category)
    Tags = models.TextField(null=True, blank=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title