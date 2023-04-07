from django.http import Http404
from .models.Profile import Profile
from .models.WorkExperience import WorkExperience


def check_profile_is_owner_skill(profile, skill_id):
    owner = WorkExperience.objects.get(id=skill_id).owner
    if profile != owner:
        raise Http404("You don't have permission to edit this profile")


def search_profiles(search_query=""):
    searched_profiles = Profile.objects.all()
    return searched_profiles
