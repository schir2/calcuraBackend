from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        """
        Return the URL that the user clicks in the verification email.
        Instead of the default /accounts/confirm-email/<key>/,
        we point to the front-end at localhost:3000 or your production domain.
        """

        key = emailconfirmation.key

        url = f"{settings.FRONTEND_URL}/verify?key={key}"

        return url
