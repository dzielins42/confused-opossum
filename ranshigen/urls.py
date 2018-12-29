from django.urls import path, include
from .views import GeneratorViewSet, GenerateView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('generators', GeneratorViewSet)
router.register('generate', GenerateView, base_name='generate')

urlpatterns = [
    path('api/', include(router.urls)),
]
