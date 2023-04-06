from django.contrib import admin
from .models.Job import Job
from .models.JobLevel import JobLevel
from .models.AppliedCV import AppliedCV

# Register your models here.
admin.site.register(Job)
admin.site.register(JobLevel)
admin.site.register(AppliedCV)