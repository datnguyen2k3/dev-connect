from django.db import models
import uuid
from app.projects.models.SkillTag import SkillTag


class Company(models.Model):
    COMPANY_TYPE = (
        ("Outsourcing", "Outsourcing"),
        ("Product", "Product"),
    )

    WORKING_TIME = (
        ("Monday - Friday", "Monday - Friday"),
        ("Monday - Saturday", "Monday - Saturday"),
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
    type = models.CharField(
        max_length=200,
        choices=COMPANY_TYPE,
        blank=True,
        null=True,
        default="Outsourcing",
    )
    working_time = models.CharField(
        max_length=200,
        choices=WORKING_TIME,
        blank=True,
        null=True,
        default="Monday - Friday",
    )
    number_employees = models.CharField(
        max_length=200, choices=NUMBER_EMPLOYEES, blank=True, null=True
    )
    overview = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(SkillTag, blank=True, null=True)
    advantage = models.TextField(blank=True, null=True)
    company_img = models.ImageField(
        null=True, blank=True, default="companies/default.jpg", upload_to="companies/"
    )
    # base_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    cities = models.CharField(max_length=200, default="", null=True, blank=True)

    def __str__(self):
        return self.name

    def average_salary_stars(self):
        total = sum([review.salary_stars for review in self.companyreview_set.all()])
        return total / len(self.companyreview_set.all())

    def average_training_stars(self):
        total = 0
        for review in self.companyreview_set.all():
            total += review.training_stars
        return total / len(self.companyreview_set.all())

    def average_employee_attention_stars(self):
        total = 0
        for review in self.companyreview_set.all():
            total += review.employee_attention_stars
        return total / len(self.companyreview_set.all())

    def average_culture_stars(self):
        total = 0
        for review in self.companyreview_set.all():
            total += review.culture_stars
        return total / len(self.companyreview_set.all())

    def average_office_starts(self):
        total = 0
        for review in self.companyreview_set.all():
            total += review.office_starts
        return total / len(self.companyreview_set.all())

    def average_stars(self):
        total = 0
        for review in self.companyreview_set.all():
            total += review.stars
        return total / len(self.companyreview_set.all())

    class Meta:
        ordering = ["-id"]
        indexes = [
            models.Index(fields=["id"]),
        ]
