from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.projects.models import Project
from .serializers import ProjectSerializer, ReviewSerializer
from app.projects.models import Review
from app.projects.utils import add_review


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


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_review_view(request, project_id):
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

