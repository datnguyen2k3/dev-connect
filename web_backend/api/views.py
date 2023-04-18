from rest_framework.decorators import api_view
from rest_framework.response import Response


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


