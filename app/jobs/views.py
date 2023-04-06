from django.shortcuts import render
from .models.Job import Job
from django.contrib.auth.decorators import login_required
from .forms import AppliedCVForm

# Create your views here.
def single_job_view(request, job_id):
    
    return render(request, 'jobs/single-job.html', {})

def jobs_view(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs
    }
    
    return render(request, 'jobs/jobs.html', context=context)

def add_job_view(request):
    pass

def edit_job_view(request, job_id):
    pass

def delete_job_view(request, job_id):
    pass

def applied_cvs_view(request, job_id):
    pass

@login_required(login_url="user_auth:login")
def applied_cv_form_view(request, job_id):
    pass
    user = request.user.profile
    job = Job.objects.get(pk=job_id)
    
    form = AppliedCVForm(request.POST or None, request.FILES or None)
    