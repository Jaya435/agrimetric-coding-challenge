import json

import pytest
from model_bakery import baker
from ..models import Sandwich

pytestmark = pytest.mark.django_db


class TestSandwichEndpoints:

    endpoint = "/api/sandwich/"

    def test_list(self, api_client):
        baker.make(Sandwich, _quantity=3)

        response = api_client().get(
            self.endpoint
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create(self, api_client):
        sandwich = baker.prepare(Sandwich)
        expected_json = {
            'order_number': sandwich.order_number,
            'type': sandwich.type,
            'recipient': sandwich.recipient,
            'completed': sandwich.completed
        }

        response = api_client().post(
            self.endpoint,
            data=expected_json,
            format='json'
        )

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json

    def test_retrieve(self, api_client):
        sandwich = baker.make(Sandwich)
        expected_json = {
            'order_number': sandwich.order_number,
            'type': sandwich.type,
            'recipient': sandwich.recipient,
            'completed': sandwich.completed
        }
        url = f'{self.endpoint}{sandwich.order_number}/'

        response = api_client().get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_update(self, api_client):
        old_sandwich = baker.make(Sandwich)
        new_sandwich = baker.prepare(Sandwich)
        sandwich_dict = {
            'order_number': new_sandwich.order_number,
            'type': new_sandwich.type,
            'recipient': new_sandwich.recipient,
            'completed': new_sandwich.completed
        }

        url = f'{self.endpoint}{old_sandwich.order_number}/'

        response = api_client().put(
            url,
            sandwich_dict,
            format='json'
        )

        assert response.status_code == 200
        assert json.loads(response.content) == sandwich_dict

    @pytest.mark.parametrize('field', [
        ('type'),
        ('recipient'),
        ('completed'),
    ])
    def test_partial_update(self, field, api_client):
        sandwich = baker.make(Sandwich)
        sandwich_dict = {
            'order_number': sandwich.order_number,
            'type': sandwich.type,
            'recipient': sandwich.recipient,
            'completed': sandwich.completed
        }
        valid_field = sandwich_dict[field]
        url = f'{self.endpoint}{sandwich.order_number}/'

        response = api_client().patch(
            url,
            {field: valid_field},
            format='json'
        )

        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field

    def test_delete(self, api_client):
        sandwich = baker.make(Sandwich)
        url = f'{self.endpoint}{sandwich.order_number}/'

        response = api_client().delete(url)

        assert response.status_code == 204
        assert Sandwich.objects.all().count() == 0
