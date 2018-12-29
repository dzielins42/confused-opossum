from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Generator
from .serializers import GeneratorSerializer
from .generators import GeneratorParser

class GeneratorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Generator.objects.all()
    serializer_class = GeneratorSerializer

class GenerateView(viewsets.ViewSet):

    def list(self, request):
        id = request.query_params.get('id')
        count = request.query_params.get('count')
        if count is None:
            count = 10
        else:
            count = int(count)
        return Response(self._generate(id, count))

    def _generate(self, id, count):
        parser = GeneratorParser(self._getGenerator)
        generator = self._getGenerator(id, parser)
        return generator.generate(count)

    def _getGenerator(self, id, parser):
        generator = Generator.objects.get(res_id=id)
        return parser.parse(generator.definition)
