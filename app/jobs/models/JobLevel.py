from django.db import models


class JobLevel(models.Model):
    LEVELS = (
        ("intern", "Intern"),
        ("fresher", "Fresher"),
        ("junior", "Junior"),
        ("mid", "Mid"),
        ("senior", "Senior"),
        ("manager", "Manager"),
        ("director", "Director"),
    )

    id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=200, choices=LEVELS, blank=True, null=True)

    def __str__(self):
        return self.level
