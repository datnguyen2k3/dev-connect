import os
from django.db.models.signals import post_save, post_delete, pre_save
from django.contrib.auth.models import User
from .models import Profile


def create_profile_after_create_user(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        
        
def update_user_after_update_profile(sender, instance, created, **kwargs):
    if not instance.user:
        return
    
    user = instance.user
    if not created:
        user.username = instance.username
        user.email = instance.email
        user.first_name = instance.name
        user.save()


def delete_user_after_delete_profile(sender, instance, **kwargs):
    if instance.user:
        user = instance.user
        user.delete()
    
    
post_save.connect(update_user_after_update_profile, sender=Profile)
post_save.connect(create_profile_after_create_user, sender=User)
post_delete.connect(delete_user_after_delete_profile, sender=Profile)
