from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from devsearch.utils import CustomPaginator
from .utils import (
    check_profile_is_project_owner,
    search_projects,
    add_review,
    update_project,
    add_project,
)
from .forms import ProjectForm
from .models import Project, Review


# Create your views here.
def projects_view(request):
    search_query = ""
    page_number = 1
    
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    if request.GET.get("page_number"):
        page_number = int(request.GET.get("page_number"))

    searched_projects = search_projects(search_query)
    custom_paginator = CustomPaginator(searched_projects)
    searched_page = custom_paginator.page(page_number)
    page_range = custom_paginator.get_page_range_in_search_template(page_number)

    context = {
        "search_query": search_query,
        "searched_page": searched_page,
        "page_range": page_range,
    }

    return render(request, "projects/projects.html", context=context)


def single_project_view(request, project_id):
    if request.method == "POST":
        add_review(request, project_id)
        return redirect("projects:single-project", project_id=project_id)

    project = Project.objects.get(pk=project_id)
    context = {"project": project}
    return render(request, "projects/single_project.html", context=context)


@login_required(login_url="devsearch_auth:login")
def create_project_view(request):
    if add_project(request):
        return redirect("users:account")

    project_form = ProjectForm()
    context = {"form": project_form}
    return render(request, "projects/project_form.html", context=context)


@login_required(login_url="devsearch_auth:login")
def edit_project_view(request, project_id):
    edited_project = Project.objects.get(id=project_id)

    if edited_project.owner != request.user.profile:
        return Http404("You don't have permission to edit this project")

    if update_project(request, project_id):
        return redirect("users:account")

    project_form = ProjectForm(instance=edited_project)
    context = {"form": project_form}
    return render(request, "projects/project_form.html", context=context)


@login_required(login_url="devsearch_auth:login")
def delete_project_view(request, project_id):
    deleted_project = Project.objects.get(id=project_id)

    if deleted_project.owner != request.user.profile:
        return Http404("You don't have permission to delete this project")

    if request.method == "POST":
        deleted_project.delete()
        return redirect("users:account")

    return render(request, "projects/delete_project.html")
