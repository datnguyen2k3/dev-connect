from .models.Project import Project


def search_projects(search_query=""):
    projects = Project.objects.all()
    return projects
