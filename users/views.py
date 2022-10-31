from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

from datetime import datetime
from config.settings import SECRET_KEY
import jwt
from rest_framework import status
from .serializers import UserSerializer
from .models import Tokens, Users
from parents.models import Parents
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class Register(generics.ListCreateAPIView):

    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def post(self, request):

        return self.create(request)


class SignIn(generics.GenericAPIView, mixins.CreateModelMixin):

    queryset = Users.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(operation_summary='Sign in with existing user', operation_description="""
            - You must be registered to sign in
            - You will get a token after signing in
            - You must use the token to access the other endpoints
        """
                         )
    def post(self, request):
        try:
            # get request data
            [email, password] = [request.data['email'],
                                 request.data['password']]

            # trying to get account by email and password
            print(email)
            account = Users.objects.get(
                email=email, password=password)

            # generate token
            token = jwt.encode({'email': email, 'password': password, 'timestamp': datetime.timestamp(
                datetime.now())}, SECRET_KEY, algorithm='HS256')
            print(account.parent.id)
            # generate token object
            newToken = {
                'token': token,
                'parent_id': account.parent.id
            }

            # save token in database
            Tokens.objects.create(**newToken)

            return Response({'token': token}, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({'message': 'email or password wrong!'}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'message': 'Parent is registered with another account!'}, status=status.HTTP_400_BAD_REQUEST)
