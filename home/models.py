from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    Extends the built-in django user model to include additional user information.
    """

    user=models.OneToOneField(User, on_delete=models.CASCADE)


    mame=models.CharField(max_length=100, blank=True)
    email=models.EmailField(max_length=150, blank=True)
    phone_numer=models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a profile instance when a new user is created.
    """
    instance.profile.save()

# Create your models here.
