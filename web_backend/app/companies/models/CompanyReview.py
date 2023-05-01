import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from app.users.models.Profile import Profile
from app.companies.models.Company import Company


class CompanyReview(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=True, default=uuid.uuid4
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default="")

    advantage = models.TextField(blank=True, null=True)
    defect = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    salary_stars = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    training_stars = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    employee_attention_stars = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    culture_stars = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    office_starts = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    @property
    def stars(self):
        return (
                self.salary_stars
                + self.training_stars
                + self.employee_attention_stars
                + self.culture_stars
                + self.office_starts
        ) // 5

    def __str__(self):
        return ""

    class Meta:
        ordering = ["-created"]
        unique_together = ["company", "user"]
