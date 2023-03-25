from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.projects.models import Project
from .serializers import ProjectSerializer


# Create your views here.
@api_view(["GET"])
def get_routes_view(request):
    routes = [
        {"GET": "api/projects/"},
        {"GET": "api/projects/id"},
    ]

    return Response(routes)


@api_view(["GET"])
def get_projects_view(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_single_project_view(request, project_id):
    project = Project.objects.get(pk=project_id)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
