from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_user_view(request):
    if not request.user.is_superuser:
        return Response("You are not an admin")

    if not request.data.get("username"):
        return Response("Username is required")

    username = request.data.get("username")

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("User does not exist")

    profile = user.profile
    profile.delete()
    return Response("User is deleted")


@api_view(["GET"])
def get_number_login_user(request):
    import redis

    r = redis.Redis(host='localhost', port=6379, db=1)

    keys = r.scan_iter(match=':1:django.contrib.sessions.cache*')
    count = 0
    for key in keys:
        count += 1
    return Response(count)
