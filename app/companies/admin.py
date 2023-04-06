from django.contrib import admin
from .models.Company import Company
from .models.CompanyReview import CompanyReview


# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyReview)



