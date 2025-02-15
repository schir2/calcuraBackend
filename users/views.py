import json
from django.db.utils import IntegrityError

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

User = get_user_model()


@require_POST
@csrf_protect
def login_view(request):
    """Authenticate user and create a session."""
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"message": "Login successful"}, status=status.HTTP_200_OK)
    return JsonResponse({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@require_POST
@csrf_protect
def logout_view(request):
    """Logout user and remove session."""
    logout(request)
    return JsonResponse({"message": "Logged out successfully"}, status=status.HTTP_200_OK)


@require_POST
@csrf_protect
def register_view(request):
    """
    Register a new user. Optionally send a verification email here.
    """
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")


    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "User already exists"}, status=400)

    user = User(username=username, is_active=True)
    user.set_password(password)

    try:
        user.save()
    except IntegrityError as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({
        "message": "Registration successful",
        "user": {
            "username": user.username,
            "email": user.email
        }
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def get_csrf_token(request):
    """Return CSRF token so frontend can include it in requests."""
    return Response({"csrfToken": get_token(request)}, status=status.HTTP_200_OK)
