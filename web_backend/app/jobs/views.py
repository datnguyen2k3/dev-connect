from django.shortcuts import render, redirect
from .models.Job import Job
from django.contrib.auth.decorators import login_required
from .forms import AppliedCVForm
from .utils import search_jobs
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models.AppliedCV import AppliedCV


# Create your views here.
def single_job_view(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, "jobs/single-job.html", {"job": job})


def jobs_view(request):
    jobs = search_jobs(request.GET)

    context = {
        "number_jobs": len(jobs),
        "jobs": jobs
    }
    
    return render(request, "jobs/jobs.html", context=context)


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
    user = request.user.profile
    job = Job.objects.get(pk=job_id)

    form = AppliedCVForm()

    if request.method == "POST":
        form = AppliedCVForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "jobs/cv_form.html", {"form": form})
        
        if AppliedCV.objects.filter(Q(owner=user) & Q(job=job)).exists():
            delete_cv = AppliedCV.objects.filter(Q(owner=user) & Q(job=job))
            delete_cv.delete()

        new_cv = form.save(commit=False)
        new_cv.job = job
        new_cv.owner = user
        new_cv.save()
        return redirect("jobs:single-job", job_id=job_id)

    return render(request, "jobs/cv_form.html", {"form": form})
