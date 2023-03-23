from django.db.models import Q
from django.http import Http404
from .models import Profile, Skill


def check_profile_is_owner_skill(profile, skill_id):
    owner = Skill.objects.get(id=skill_id).owner
    if profile != owner:
        raise Http404("You don't have permission to edit this profile")


def search_profiles(request) -> list[Profile]:
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    skills = Skill.objects.filter(name__icontains=search_query)

    searched_profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)
        | Q(short_intro__icontains=search_query)
        | Q(skill__in=skills)
    )

    return (search_query, searched_profiles)

