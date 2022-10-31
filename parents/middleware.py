from rest_framework import authentication, exceptions
from users.models import Tokens


class Authenticate(authentication.BaseAuthentication):
    def authenticate(self, request):
        sent_token = request.headers.get('jwt')
        for token_object in Tokens.objects.all():
            if token_object.token == sent_token:
                return (True, None)
        raise exceptions.AuthenticationFailed('You are not authenticated!')
