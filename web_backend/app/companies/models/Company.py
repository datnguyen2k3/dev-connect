from django.db import models
import uuid
from app.projects.models.SkillTag import SkillTag

class Company(models.Model):
    COMPANY_TYPE = (
        ("outsourcing", "Outsourcing"),
        ("product", "Product"),
    )

    WORKING_TIME = (
        ("t2_t6", "Monday - Friday"),
        ("t2_t7", "Monday - Saturday"),
    )

    NUMBER_EMPLOYEES = (
        ("1-10", "1-10"),
        ("11-50", "11-50"),
        ("51-100", "51-100"),
        ("101-500", "101-500"),
        ("501-1000", "501-1000"),
        ("1000+", "1000+"),
    )

    id = models.UUIDField(
        primary_key=True, unique=True, editable=True, default=uuid.uuid4
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, choices=COMPANY_TYPE, blank=True, null=True)
    working_time = models.CharField(
        max_length=200, choices=WORKING_TIME, blank=True, null=True
    )
    number_employees = models.CharField(
        max_length=200, choices=NUMBER_EMPLOYEES, blank=True, null=True
    )
    overview = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(SkillTag, blank=True, null=True)
    advantage = models.TextField(blank=True, null=True)

    # base_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # cities = models.ManyToManyField(City, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        indexes = [
            models.Index(fields=["id"]),
        ]
