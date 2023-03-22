from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect
from devsearch.utils import CustomPaginator
from .models import Profile, Skill
from django.contrib.auth import authenticate, login, logout



def check_profile_is_owner_skill(profile, skill_id):
    owner = Skill.objects.get(id=skill_id).owner
    if profile != owner:
        raise Http404("You don't have permission to edit this profile")


def search_profiles(request) -> list[Profile]:
    search_query = ''
    
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    
    skills = Skill.objects.filter(name__icontains=search_query)
    
    searched_profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)
        | Q(short_intro__icontains=search_query)
        | Q(skill__in=skills)
    )

    return (search_query, searched_profiles)


def login_web(request):
    username = request.POST["username"]
    password = request.POST["password"]

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.error(request, "User does not exist")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return True
    else:
        messages.error(request, "Username or password is incorrect")
        return False