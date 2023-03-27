from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.projects.models import Project
from .serializers import ProjectSerializer, ReviewSerializer
from app.projects.models import Review
from app.projects.utils import add_review, update_project


# Create your views here.
@api_view(["GET"])
def get_routes_view(request):
    routes = [
        {"GET": "api/projects/"},
        {"GET": "api/projects/id"},
        {"POST": "api/projects/id/edit"},
        {"POST": "api/projects/id/reviews/add"},
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


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def edit_project_view(request, project_id):
    edited_project = Project.objects.get(id=project_id)

    if edited_project.owner != request.user.profile:
        return Response("You don't have permission to edit this project")

    if not update_project(request, project_id):
        return Response("Have a problem with updating project")

    return Response("Project updated")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_review_view(request, project_id):
    if request.method != "POST":
        return Response("Method not allowed")

    new_review = add_review(request, project_id)
    review_serializer = ReviewSerializer(new_review, many=False)
    print(review_serializer.data)
    return Response(review_serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_single_review_view(request, project_id, review_id):
    review = Review.objects.get(pk=review_id)
    serializer = ReviewSerializer(review, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def get_reviews_view(request, project_id):
    reviews = Review.objects.filter(project=project_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_review_view(request, project_id, review_id):
    review = Review.objects.get(pk=review_id)

    if review.owner != request.user.profile:
        return Response("You are not the owner of this review")

    review.delete()
    return Response("Review deleted")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def edit_review_view(request, project_id, review_id):
    review = Review.objects.get(pk=review_id)

    if review.owner != request.user.profile:
        return Response("You are not the owner of this review")

    if request.method != "POST":
        return Response("Method not allowed")

    review.body = request.POST["comment"]
    review.save()
    return Response("Review updated")
