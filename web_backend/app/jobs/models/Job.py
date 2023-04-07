import uuid
from django.db import models
from app.companies.models.Company import Company
from app.projects.models.SkillTag import SkillTag
from .JobLevel import JobLevel


class Job(models.Model):
    WORKING_MODELS = (
        ("office", "At Office"),
        ("remote", "Remote"),
        ("hybrid", "Hybrid"),
    )

    TIME_WORKS = (
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("full_time_part_time", "Full Time or Part Time"),
    )

    id = models.UUIDField(
        primary_key=True, unique=True, editable=True, default=uuid.uuid4
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    skills = models.ManyToManyField(SkillTag, blank=True)
    levels = models.ManyToManyField(JobLevel, blank=True)
    # locations = models.ManyToManyField(Location, blank=True)

    is_active = models.BooleanField(default=True)
    lower_salary = models.IntegerField(blank=True, null=True)
    upper_salary = models.IntegerField(blank=True, null=True)
    time_work = models.CharField(
        max_length=200, choices=TIME_WORKS, blank=True, null=True
    )
    working_model = models.CharField(
        max_length=200, choices=WORKING_MODELS, blank=True, null=True
    )
    title = models.CharField(max_length=200, blank=True, null=True)

    advantage = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    benefit = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    job_img1 = models.ImageField(
        upload_to="jobs/", default="jobs/default.jpg", blank=True, null=True
    )
    job_img2 = models.ImageField(
        upload_to="jobs/", default="jobs/default.jpg", blank=True, null=True
    )
    job_img3 = models.ImageField(
        upload_to="jobs/", default="jobs/default.jpg", blank=True, null=True
    )

    def __str__(self):
        return self.company.name + " - " + self.title

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["id"]),
        ]
