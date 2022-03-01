import pytest
from model_bakery import baker

from ..models import Sandwich
from ..serializers import SandwichListSerializer, SandwichSerializer

pytestmark = pytest.mark.django_db


class TestSandwichSerializer:
    def test_serialize_model(self):
        sandwich = baker.make(Sandwich)
        serializer = SandwichSerializer(sandwich)
        assert serializer.data


class TestSandwichListSerializer:
    def test_seralized_data(self):
        expected_data = {
            "sequence": 1,
            "schedule": "00:00",
            "type": "Ham sandwich",
            "task": "Make Sandwich",
            "order_number": 1,
            "recipient": "Anon",
        }
        serializer = SandwichListSerializer(data=expected_data)
        serializer.is_valid()
        assert serializer.data == expected_data
