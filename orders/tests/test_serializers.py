import pytest
from ..serializers import SandwichSerializer

from ..models import Sandwich

pytestmark = pytest.mark.django_db


class TestSandwichSerializer:
    def test_serialize_model(self):
        serializer = SandwichSerializer()

        assert serializer.data

    def test_serialized_data(self):
        data = {
            "order": 1,
            "task": Sandwich.MAKE
        }
        serializer = SandwichSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.errors == {}