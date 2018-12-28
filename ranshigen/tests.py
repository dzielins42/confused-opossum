from django.urls import reverse
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status
from .models import Generator
from .serializers import GeneratorSerializer
from .views import GeneratorViewSet

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_generator(name="", description="", res_id=""):
        if name != "":
            Generator.objects.create(name=name, description=description, res_id=res_id)

    def setUp(self):
        self.create_generator("test1", "test1")
        self.create_generator("test2", "test2")
        self.create_generator("test3", "test3")
        self.create_generator("test4", "test4")


class GetAllGeneratorsTest(BaseViewTest):

    def test_get_all_generators(self):
        request = APIRequestFactory().get("")
        view = GeneratorViewSet.as_view({'get': 'list'})
        response = view(request)
        expected = Generator.objects.all()
        serialized = GeneratorSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
