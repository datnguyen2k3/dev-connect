from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app.users.forms import ProfileForm, SkillForm
from app.users.models import Profile, Skill
from app.users.utils import check_profile_is_owner_skill, search_profiles
from devsearch.utils import CustomPaginator


# Create your views here.
def profiles_view(request):
    search_query = ""
    page_number = 1

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    if request.GET.get("page_number"):
        page_number = int(request.GET.get("page_number"))

    searched_profiles = search_profiles(search_query)
    custom_paginator = CustomPaginator(searched_profiles)
    searched_page = custom_paginator.page(page_number)
    page_range = custom_paginator.get_page_range_in_search_template(page_number)

    context = {
        "search_query": search_query,
        "searched_page": searched_page,
        "page_range": page_range,
    }

    return render(request, "users/profiles.html", context=context)


def single_profile_view(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {
        "profile": profile,
    }
    return render(request, "users/single-profile.html", context=context)


@login_required(login_url="devsearch_auth:login")
def account_view(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request, "users/account.html", context=context)


@login_required(login_url="devsearch_auth:login")
def edit_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    profile_form = ProfileForm(instance=profile)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("users:account")
        else:
            messages.error(request, "Profile is not valid!")

    return render(request, "users/profile-form.html", {"form": profile_form})


@login_required(login_url="devsearch_auth:login")
def add_skill_view(request):
    skill_form = SkillForm()
    if request.method == "POST":
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill = skill_form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
        else:
            messages.error(request, "Skill is not valid!")

        return redirect("users:account")

    return render(request, "users/skill-form.html", {"form": skill_form})


@login_required(login_url="devsearch_auth:login")
def edit_skill_view(request, skill_id):
    check_profile_is_owner_skill(request.user.profile, skill_id)
    skill = Skill.objects.get(id=skill_id)
    skill_form = SkillForm(instance=skill)

    if request.method == "POST":
        skill_form = SkillForm(request.POST, instance=skill)
        if skill_form.is_valid:
            skill_form.save()
            return redirect("users:account")

    return render(request, "users/skill-form.html", {"form": skill_form})


@login_required(login_url="devsearch_auth:login")
def delete_skill_view(request, skill_id):
    check_profile_is_owner_skill(request.user.profile, skill_id)
    skill = Skill.objects.get(id=skill_id)

    if request.method == "POST":
        skill.delete()
        return redirect("users:account")

    return render(request, "users/delete-skill.html", {"skill": skill})
