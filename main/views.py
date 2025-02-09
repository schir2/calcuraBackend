import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny


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
        return JsonResponse({"message": "Login successful", "user": {"username": user.username, "email": user.email}})
    else:
        return JsonResponse({"error": "Invalid credentials"}, status=400)

@require_POST
def logout_view(request):
    """Logout user and remove session."""
    logout(request)
    return JsonResponse({"message": "Logged out successfully"})


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def get_csrf_token(request):
    """Return CSRF token so frontend can include it in requests."""
    return JsonResponse({"csrfToken": get_token(request)})
