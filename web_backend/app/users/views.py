from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app.users.forms import ProfileForm, WorkExperienceForm, MessageForm
from app.users.models.Profile import Profile
from app.users.models.WorkExperience import WorkExperience
from app.users.models.Message import Message
from app.users.utils import check_profile_is_owner_skill, search_profiles
from src.utils import CustomPaginator


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


@login_required(login_url="user_auth:login")
def account_view(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request, "users/account.html", context=context)


@login_required(login_url="user_auth:login")
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


@login_required(login_url="user_auth:login")
def add_work_experience_view(request):
    skill_form = WorkExperienceForm()
    if request.method == "POST":
        skill_form = WorkExperienceForm(request.POST)
        if skill_form.is_valid():
            skill = skill_form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
        else:
            messages.error(request, "Skill is not valid!")

        return redirect("users:account")

    return render(request, "users/work-experience-form.html", {"form": skill_form})


@login_required(login_url="user_auth:login")
def edit_work_experience_view(request, skill_id):
    check_profile_is_owner_skill(request.user.profile, skill_id)
    skill = WorkExperience.objects.get(id=skill_id)
    skill_form = WorkExperienceForm(instance=skill)

    if request.method == "POST":
        skill_form = WorkExperienceForm(request.POST, instance=skill)
        if skill_form.is_valid:
            skill_form.save()
            return redirect("users:account")

    return render(request, "users/work-experience-form.html", {"form": skill_form})


@login_required(login_url="user_auth:login")
def delete_work_experience_view(request, skill_id):
    check_profile_is_owner_skill(request.user.profile, skill_id)
    work_experience = WorkExperience.objects.get(id=skill_id)

    if request.method == "POST":
        work_experience.delete()
        return redirect("users:account")

    return render(
        request,
        "users/delete-work-experience.html",
        {"work_experience": work_experience},
    )


@login_required(login_url="devsearch_auth:login")
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {"messageRequests": messageRequests, "unreadCount": unreadCount}
    return render(request, "users/inbox.html", context=context)


@login_required(login_url="devsearch_auth:login")
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)

    if message.is_read == False:
        message.is_read = True
        message.save()

    context = {"message": message}
    return render(request, "users/message.html", context=context)


@login_required(login_url="devsearch_auth:login")
def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, "Your message was successfully sent!")
            return redirect("users:single-profile", profile_id=recipient.id)

    context = {"recipient": recipient, "form": form}
    return render(request, "users/message-form.html", context)
