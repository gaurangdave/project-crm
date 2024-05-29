# Create your views here.
from django.shortcuts import render
from .models import Greetings
from rest_framework import generics
from .serializers import GreetingsSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GreetingsCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Greetings.objects.all(),
    serializer_class = GreetingsSerializer


class GreetingsList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Greetings.objects.all()
    serializer_class = GreetingsSerializer


class UserCreate (APIView):
    # API endpoint that allows user to be created.
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
