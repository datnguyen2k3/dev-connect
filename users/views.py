from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationFrom
from django.contrib import messages
from .models import Profile, Skill
from projects.models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, SkillForm

# Create your views here.
def profiles_view(request):
    profiles = Profile.objects.all()
    
    context = {
        'profiles':profiles
    }
    
    return render(request, 'users/profiles.html', context=context)

def single_profile_view(request, profile_id):
    context = {}
    
    try:
        profile = Profile.objects.get(id=profile_id)
        context['profile'] = profile
    except Profile.DoesNotExist:
        return Http404('Profile does not exist')
    
    return render(request, 'users/single-profile.html', context=context)


def login_view(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('users:profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('users:profiles')
        else:
            messages.error(request, 'Username or password is incorrect')
            
               
    return render(request, 'users/login-register.html', {'page':page})

def logout_view(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('users:login')

def register_view(request):
    page = 'register'
    form = CustomUserCreationFrom()
    
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User was created successfully')
            login(request, user)
            return redirect('users:profiles')
        else:
            messages.error(request, 'An error has occurred during registration')
    
    return render(request, 'users/login-register.html', {'page':page, 'form':form}) 

@login_required(login_url='users:login')
def account_view(request):
    
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    
    
    context = {
        'profile':profile
    }
    
    return render(request, 'users/account.html', context=context)

@login_required(login_url='users:login')
def edit_profile_view(request):
    try:
        profile=Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return Http404('Profile does not exist')
    
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect('users:account')
        else:
            messages.error(request, "Profile is not valid!")
            
    
    return render(request, 'users/profile-form.html', {'form':form})


@login_required(login_url='users:login')
def add_skill_view(request):
    try:
        profile=Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return Http404('Profile does not exist')
    
    form = SkillForm()
    
    if request.method == 'POST':
        form = SkillForm(request.POST)
        
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
        else:
            messages.error(request, "Skill is not valid!")
            
        return redirect('users:account')
            
    
    return render(request, 'users/skill-form.html', {'form':form})
    
@login_required(login_url='users:login')
def edit_skill_view(request, skill_id):
    try:
        skill = Skill.objects.get(id=skill_id)
    except Skill.DoesNotExist:
        return Http404('Page does not exist')
    
    form = SkillForm(instance=skill)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid:
            form.save()
            return redirect('users:account')
        
    return render(request, 'users/skill-form.html', {'form':form})

def delete_skill_view(request, skill_id):
    try:
        skill = Skill.objects.get(id=skill_id)
    except Skill.DoesNotExist:
        return Http404('Page does not exist')
    
    if request.method == 'POST':
        skill.delete()
        return redirect('users:account')
    
    return render(request, 'users/delete-skill.html', {'skill':skill})