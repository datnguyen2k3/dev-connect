from django.contrib import admin
from .models.Profile import Profile
from .models.WorkExperience import WorkExperience

# Register your models here.
admin.site.register(Profile)
admin.site.register(WorkExperience)


