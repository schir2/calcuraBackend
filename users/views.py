import json

from allauth.account.models import EmailConfirmationHMAC, EmailConfirmation
from allauth.account.utils import setup_user_email
from django.db import transaction
from allauth.account.utils import send_email_confirmation

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
@transaction.atomic
def register_view(request):
    """
    Register a new user. Optionally send a verification email here.
    """
    data = json.loads(request.body)
    email = data.get("username")
    password = data.get("password")


    if User.objects.filter(email=email).exists():
        return JsonResponse({"error": "User already exists"}, status=400)

    user = User.objects.create_user(email=email, username=email, password=password)

    setup_user_email(request, user, [])
    send_email_confirmation(request, user, signup=True)

    return JsonResponse({
        "message": "Registration successful",
        "user": {
            "email": user.email
        }
    }, status=status.HTTP_201_CREATED)


@require_POST
@csrf_protect
@transaction.atomic
def verify_view(request):
    data = json.loads(request.body)
    key = data.get("key")
    email_confirmation = EmailConfirmationHMAC.from_key(key)
    if not email_confirmation:
        try:
            email_confirmation = EmailConfirmation.objects.get(key=key)
        except EmailConfirmation.DoesNotExist:
            return JsonResponse(
                {"error": "Invalid or expired confirmation key."},
                status=status.HTTP_400_BAD_REQUEST
            )

    email_confirmation.confirm(request)
    user = email_confirmation.email_address.user
    user.is_active = True
    user.save()
    login(request, user, backend="django.contrib.auth.backends.ModelBackend")

    return JsonResponse({"message": "Email verified. You can now log in."}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def get_csrf_token(request):
    """Return CSRF token so frontend can include it in requests."""
    return Response({"csrfToken": get_token(request)}, status=status.HTTP_200_OK)
