import pytest
from model_bakery import baker
from ..serializers import SandwichSerializer

from ..models import Sandwich

pytestmark = pytest.mark.django_db


class TestSandwichSerializer:
    def test_serialize_model(self):
        sandwich = baker.make(Sandwich)
        serializer = SandwichSerializer(sandwich)

        assert serializer.data
