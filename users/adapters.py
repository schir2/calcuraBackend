from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, email_confirmation):
        """
        Return the URL that the user clicks in the verification email.
        Instead of the default /accounts/confirm-email/<key>/,
        we point to the front-end at localhost:3000 or your production domain.
        """

        key = email_confirmation.key

        url = f"{settings.FRONTEND_URL}/auth/verify?key={key}"

        return url
