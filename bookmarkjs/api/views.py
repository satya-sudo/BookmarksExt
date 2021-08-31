from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import  Response
from rest_framework import status

import json

from rest_framework.views  import APIView

from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import UserRegisterSerializer


def apiconfig(request):
    """
        API config page
        this the main page for the API
        so we can see what endpoints are available
    """


    api_urls = {
        '/login' : 'login',
        '/register' : 'register',
    }

    return JsonResponse(api_urls)



class RegisterView(APIView):

    """
        this view is responsible to register a user to our database
        UserRegistrationSerializer is used here
        takes email and password and password1(confirm password)
        return email , refresh token and access token 
        access token tells the B.E. which user is the one making the request 
        while this token has an expiry time
        if this token is expired we can use the refresh token to get back a new access token 

    """

    serializer_class = UserRegisterSerializer

    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token_return = {
                'username'  : user.username,
                'userEmail' : user.email,
                'refresh'   : str(refresh),
                'access'    : str(refresh.access_token) 
            }

            return Response(token_return,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    