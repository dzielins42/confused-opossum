from rest_framework import serializers
from .models import Generator

class GeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generator
        fields = ('id', 'name', 'description', 'res_id')
