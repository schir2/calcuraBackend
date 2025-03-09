from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import Profile
from users.serializers import UserSerializer, ProfileSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    allowed_methods = ('get', 'post',)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=['get'])
    def me(self, request):
        if not request.user.is_authenticated:
            return Response({
                "message": "You are not logged in",
            },
                status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().select_related('user')
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.id)