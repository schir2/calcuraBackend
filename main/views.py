from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CookieTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        if 'refresh' in response.data:
            refresh_token = response.data['refresh']

            response.set_cookie(
                'refresh_token',
                refresh_token,
                max_age=7 * 24 * 60 * 60,
                httponly=True,
                secure=True,
                samesite='None',
                path='/'
            )
        return response

class CookieTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        if 'refresh' not in request.data:
            cookie_refresh = request.COOKIES.get('refresh_token')
            if cookie_refresh:
                request.data['refresh'] = cookie_refresh
        return super().post(request, *args, **kwargs)