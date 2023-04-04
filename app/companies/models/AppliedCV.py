import uuid
from django.db import models
from app.users.models.Profile import Profile


class AppliedCV(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=True, default=uuid.uuid4
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cv_file = models.FileField(upload_to="cv_files", blank=True, null=True)
    intro = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.owner.username + " " + self.cv_file.name
