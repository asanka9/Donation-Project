from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pic')
    user_description = models.TextField(default='~')

    def __str__(self):
        return f'{self.user.username} Profile'




@receiver(post_save,sender=User)
def user_is_created(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()