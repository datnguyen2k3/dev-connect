import os
from django.db.models.signals import post_save, post_delete, pre_save
from django.contrib.auth.models import User
from .models import Profile


def createProfileAfterCreateUser(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        print('Profile created!')


def deleteUserAfterDeleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    
post_save.connect(createProfileAfterCreateUser, sender=User)
post_delete.connect(deleteUserAfterDeleteProfile, sender=Profile)
