from django.contrib import admin
from .models.Profile import Profile
from .models.WorkExperience import WorkExperience
from .models.Message import Message

# Register your models here.
admin.site.register(Profile)
admin.site.register(WorkExperience)
admin.site.register(Message)
