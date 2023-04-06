from django.db import models
import uuid


class Company(models.Model):
    COMPANY_TYPE = (
        ("outsourcing", "Outsourcing"),
        ("product", "Product"),
    )
    
    WORKING_TIME = (
        ('t2_t6', 'Monday - Friday'),
        ('t2_t7', 'Monday - Saturday'),
    )

    id = models.UUIDField(
        primary_key=True, unique=True, editable=True, default=uuid.uuid4
    )

    name = models.CharField(max_length=200, blank=True, null=True)
    # cities = models.ManyToManyField(City, blank=True)
    type = models.CharField(max_length=200, choices=COMPANY_TYPE, blank=True, null=True)
    working_time = models.CharField(max_length=200, choices=WORKING_TIME, blank=True, null=True)

    # base_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
