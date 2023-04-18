import uuid
from django.db import models
from app.users.models.Profile import Profile
from app.projects.models.SkillTag import SkillTag


class Project(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_img = models.ImageField(
        null=True, blank=True, default="projects/default.jpg", upload_to="projects/"
    )
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    skill_tags = models.ManyToManyField(SkillTag, blank=True)
    upvote_users = models.ManyToManyField(
        Profile, related_name="upvote_projects", blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["id"]),
        ]
