from django.shortcuts import render
from .models.Company import Company

# Create your views here.

def single_company_view(request):
    pass

def companies_view(request):
    
    companies = Company.objects.all()
    
    
    context = {
        'companies': companies,
        'number_companies': len(companies),
    }

    
    return render(request, 'companies/companies.html', context=context)

def company_jobs_view(request, company_id):
    company = Company.objects.get(id=company_id)
    
    return render(request, 'companies/single-company-jobs.html', context={'company': company})

def add_company_view(request):
    pass

def edit_company_view(request):
    pass

def delete_company_view(request):
    pass

def company_reviews_view(request):
    pass
