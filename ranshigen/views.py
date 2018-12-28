from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Generator
from .serializers import GeneratorSerializer

class GeneratorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Generator.objects.all()
    serializer_class = GeneratorSerializer
