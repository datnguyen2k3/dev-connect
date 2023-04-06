from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from src.utils import CustomPaginator
from api.app.projects.serializers import ProjectSerializer, ReviewSerializer
from app.projects.utils import search_projects
from app.projects.models.Project import Project
from app.projects.models.ProjectComment import ProjectComment
from app.projects.forms import ProjectForm


@api_view(["GET"])
def get_projects_view(request):
    search_query = ""
    page_number = 1

    if request.data.get("search_query"):
        search_query = request.data.get("search_query")

    if request.data.get("page_number"):
        page_number = int(request.data.get("page_number"))

    searched_projects = search_projects(search_query)
    custom_paginator = CustomPaginator(searched_projects)

    if page_number < 1:
        return Response("Minimum page number is 1")

    if page_number > custom_paginator.num_pages:
        return Response("Page number is over the maximum number of pages")

    searched_page = custom_paginator.page(page_number)
    searched_projects = searched_page.object_list
    serializer = ProjectSerializer(searched_projects, many=True)

    response_data = [
        {
            "search_query": search_query,
            "number_pages": custom_paginator.num_pages,
        }
    ]
    response_data += serializer.data

    return Response(response_data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def put_project_view(request):
    project_form = ProjectForm(request.data, request.FILES)

    if not project_form.is_valid():
        return Response("Invalid form")

    project = project_form.save(commit=False)
    project.owner = request.user.profile
    project.save()
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def get_single_project_view(request, project_id):
    project = Project.objects.get(pk=project_id)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def edit_project_view(request, project_id):
    edited_project = Project.objects.get(id=project_id)
    project_form = ProjectForm(request.POST, request.FILES, instance=edited_project)

    if edited_project.owner != request.user.profile:
        return Response("You don't have permission to edit this project")

    if not project_form.is_valid():
        return Response("Invalid form")

    project = project_form.save()
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_project_view(request, project_id):
    project = Project.objects.get(pk=project_id)

    if project.owner != request.user.profile:
        return Response("You don't have permission to delete this project")

    project.delete()
    return Response("Project deleted")


@api_view(["GET"])
def get_reviews_view(request, project_id):
    reviews = ProjectComment.objects.filter(project=project_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_single_review_view(request, project_id, review_id):
    review = ProjectComment.objects.get(pk=review_id)
    serializer = ReviewSerializer(review, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def put_review_view(request, project_id):
    if not request.data.get("body"):
        return Response("Body is required")

    body = request.data.get("body")
    new_review = ProjectComment.objects.create(
        project_id=project_id,
        body=body,
        owner=request.user.profile,
    )

    review_serializer = ReviewSerializer(new_review, many=False)
    return Response(review_serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_review_view(request, project_id, review_id):
    review = ProjectComment.objects.get(pk=review_id)

    if review.owner != request.user.profile:
        return Response("You are not the owner of this review")

    review.delete()
    return Response("Review deleted")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def edit_review_view(request, project_id, review_id):
    review = ProjectComment.objects.get(pk=review_id)

    if review.owner != request.user.profile:
        return Response("You are not the owner of this review")

    review.body = request.data["comment"]
    review.save()
    serializer = ReviewSerializer(review, many=False)
    return Response(serializer.data)
