from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from devsearch.utils import CustomPaginator
from .utils import check_profile_is_project_owner, search_projects, add_review
from .forms import ProjectForm
from .models import Project, Review


# Create your views here.
def projects_view(request):
    search_query, searched_projects = search_projects(request)
    searched_page, page_range = CustomPaginator.paginate_query_set(request, searched_projects)
    
    context = {
        'search_query': search_query,
        'searched_page': searched_page,
        'page_range': page_range,
    }
    
    return render(request, "projects/projects.html", context=context)


def single_project_view(request, project_id):
    if request.method == "POST":
        add_review(request, project_id)
        return redirect("projects:single-project", project_id=project_id)
    
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
    