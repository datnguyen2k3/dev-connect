import uuid
from django.db import models
from app.users.models.Profile import Profile
from app.jobs.models.Job import Job


class AppliedCV(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=True, default=uuid.uuid4
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cv_file = models.FileField(upload_to="cv_files", blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.owner.username + " " + self.cv_file.name
