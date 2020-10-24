from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Post(models.Model):
    title = models.CharField(max_length=255)
    project_link = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="posts")
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()