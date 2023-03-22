from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from .models import Project, Review, Tag



def check_profile_is_project_owner(profile, project_id):
    owner = Project.objects.get(id=project_id).owner
    if profile != owner:
        raise Http404("You don't have permission to edit this profile")


def search_projects(request):
    search_query = ''
    
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    
    tags = Tag.objects.filter(name__icontains=search_query)
    
    searched_projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query)
        | Q(description__icontains=search_query)
        | Q(owner__name__icontains=search_query)
        | Q(tags__in=tags)
    )
    
    return (search_query, searched_projects)


@login_required(login_url="users:login")
def add_review(request, project_id):
    if request.method != "POST":
        return
    
    comment = request.POST.get("comment")
    
    review = Review.objects.create(
        body=comment,
        project_id=project_id,
        owner=request.user.profile,
    )
    
    review.save()    
    

