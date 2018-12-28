from django.urls import path, include
from .views import GeneratorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('generators', GeneratorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
