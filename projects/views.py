from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from users.models import Profile
from .forms import ProjectForm
from .models import Project


# Create your views here.
def projects_view(request):
    projects = Project.objects.all()
    context = {"projects": projects, }
    return render(request, "projects/projects.html", context=context)


def single_project_view(request, project_id):
    project = Project.objects.get(pk=project_id)
    context = {"project": project, }
    return render(request, "projects/single_project.html", context=context)


@login_required(login_url="users:login")
def create_project_view(request):
    project_form = ProjectForm()
    context = {"form": project_form, }

    if request.method == "POST":
        project_form = ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            return redirect("users:account")

    return render(request, "projects/project_form.html", context=context)


@login_required(login_url="users:login")
def edit_project_view(request, project_id):
    check_profile_is_project_owner(request.user.profile, project_id)
    edited_project = Project.objects.get(id=project_id)
    project_form = ProjectForm(instance=edited_project)

    if request.method == "POST":
        project_form = ProjectForm(request.POST, request.FILES, instance=edited_project)
        if project_form.is_valid():
            project_form.save()
            return redirect("users:account")

    context = {"form": project_form}
    return render(request, "projects/project_form.html", context=context)


@login_required(login_url="users:login")
def delete_project_view(request, project_id):
    check_profile_is_project_owner(request.user.profile, project_id)

    if request.method == "POST":
        deleted_project = Project.objects.get(id=project_id)
        deleted_project.delete()
        return redirect("users:account")

    return render(request, "projects/delete_project.html")


# Other functions
def check_profile_is_project_owner(profile, project_id):
    owner = Project.objects.get(id=project_id).owner
    if profile != owner:
        raise Http404("You don't have permission to edit this profile")

