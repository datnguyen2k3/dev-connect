import uuid
from django.db import models
from django.contrib.auth.models import User
from app.projects.models.SkillTag import SkillTag
from app.users.models.Profile import Profile

class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True
    )
    recipient = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    is_read = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ["is_read", "-created"]
