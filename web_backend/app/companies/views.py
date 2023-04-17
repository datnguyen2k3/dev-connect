from django.shortcuts import render, redirect
from .models.Company import Company
from .models.CompanyReview import CompanyReview
from .forms import CompanyReviewForm
from .utils import search_companies
from django.contrib.auth.decorators import login_required

# Create your views here.

def single_company_view(request, company_id):
    
    return redirect('companies:company-jobs', company_id=company_id)

def companies_view(request):
    
    companies = search_companies(request.GET)
    
    
    context = {
        'companies': companies,
        'number_companies': len(companies),
    }

    
    return render(request, 'companies/companies.html', context=context)

def company_jobs_view(request, company_id):
    company = Company.objects.get(id=company_id)
    
    context = {
        'company': company,
        'number_jobs': len(company.job_set.all()),
        'number_reviews': len(company.companyreview_set.all()),
    }
    
    return render(request, 'companies/single-company-jobs.html', context=context)

def add_company_view(request):
    pass

def edit_company_view(request):
    pass

def delete_company_view(request):
    pass

def company_reviews_view(request, company_id):
    company = Company.objects.get(id=company_id)
    
    context = {
        'company': company,
        'number_reviews': len(company.companyreview_set.all()),
        'number_jobs': len(company.job_set.all())
    }
    
    return render(request, 'companies/single-company-reviews.html', context=context)

@login_required(login_url='users:login')
def review_form_view(request, company_id):
    user = request.user.profile
    company = Company.objects.get(id=company_id)

    if request.POST:
        review_form = CompanyReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = user
            review.company = company
            review.save()
            return redirect('companies:single-company', company_id)
    
    context = {
        'company': company,
        
    }
    
    return render(request, 'companies/review_form.html', context=context)
