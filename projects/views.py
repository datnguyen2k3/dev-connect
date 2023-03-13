from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from .forms import ProjectForm
from .models import Project, Review, Tag

# Create your views here.
def projects_view(request):
    projects = Project.objects.all()
    
    context = {
        'projects': projects,
    }
    
    return render(request, 'projects/projects.html', context=context)

def single_project_view(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
        print(project)
    except Project.DoesNotExist:
        return HttpResponse('Project does not exist')
    
    tags = project.tags.all()
    
    context = {
        'project': project,
        'tags': tags,
    }
        
    return render(request,'projects/single_project.html', context=context)

def createProject(request):
    projectForm = ProjectForm()
    
    context = {
        'form' : projectForm,
    }
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects:projects')
    
    return render(request, 'projects/project_form.html', context=context)

def editProject(request, project_id):
    try:
        currentProject = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return HttpResponse('Project does not exist')
    
    editForm = ProjectForm(instance=currentProject)
    
    if request.method == 'POST':
        editForm = ProjectForm(request.POST, request.FILES, instance=currentProject)
        if editForm.is_valid():
            editForm.save()
            return redirect('projects:projects')
        else:
            print("error")
    
    context = {
        'form':editForm
    }
    
    return render(request, 'projects/project_form.html', context=context)

def deleteProject(request, project_id):
    if request.method != 'POST':
        return render(request, 'projects/delete_project.html')    
    
    try:
        currentProject = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return HttpResponse('Project does not exist')
    
    currentProject.delete()
    return redirect('projects:projects')
    
    
    
    
    