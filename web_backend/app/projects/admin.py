from django.contrib import admin
from .models.Project import Project
from .models.ProjectComment import ProjectComment
from .models.SkillTag import SkillTag


# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectComment)
admin.site.register(SkillTag)
