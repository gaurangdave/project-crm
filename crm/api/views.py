# Create your views here.
from django.shortcuts import render
from .models import Greetings
from rest_framework import generics
from .serializers import GreetingsSerializer


class GreetingsCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Greetings.objects.all(),
    serializer_class = GreetingsSerializer


class GreetingsList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Greetings.objects.all()
    serializer_class = GreetingsSerializer
