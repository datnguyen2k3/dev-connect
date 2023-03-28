from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from devsearch.utils import CustomPaginator
from app.projects.forms import ProjectForm
from .models import Project, Review, Tag


def check_profile_is_project_owner(profile, project_id):
    owner = Project.objects.get(id=project_id).owner
    if profile != owner:
        raise Http404("You don't have permission to edit this profile")


def search_projects(search_query=""):
    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query)
        | Q(description__icontains=search_query)
        | Q(owner__name__icontains=search_query)
        | Q(tags__in=tags)
    )

    return projects


def add_review(request, project_id):
    comment = request.POST.get("comment")

    review = Review.objects.create(
        body=comment,
        project_id=project_id,
        owner=request.user.profile,
    )

    review.save()
    return review


def update_project(request, project_id):
    if request.method != "POST":
        return False

    edited_project = Project.objects.get(id=project_id)
    if request.user.profile != edited_project.owner:
        return False

    project_form = ProjectForm(request.POST, request.FILES, instance=edited_project)
    if not project_form.is_valid():
        return False

    project_form.save()
    return True


def add_project(request):
    if request.method != "POST":
        return None

    project_form = ProjectForm(request.POST, request.FILES)
    if not project_form.is_valid():
        return None

    project = project_form.save(commit=False)
    project.owner = request.user.profile
    project.save()
    return project
