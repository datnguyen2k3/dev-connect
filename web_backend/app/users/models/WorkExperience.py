import uuid
from django.db import models
from .Profile import Profile
from app.projects.models.SkillTag import SkillTag
from app.companies.models.Company import Company


class WorkExperience(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=True, default=uuid.uuid4
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    skills = models.ManyToManyField(SkillTag, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.job_title)
