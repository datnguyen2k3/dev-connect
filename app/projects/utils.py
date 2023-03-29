from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from devsearch.utils import CustomPaginator
from app.projects.forms import ProjectForm
from .models import Project, Review, Tag

def search_projects(search_query=""):
    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query)
        | Q(description__icontains=search_query)
        | Q(owner__name__icontains=search_query)
        | Q(tags__in=tags)
    )

    return projects