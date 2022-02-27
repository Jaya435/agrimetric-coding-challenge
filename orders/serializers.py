from rest_framework import serializers

from .models import Sandwich


class SandwichSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandwich
        fields = ["order_number", "received_at", "completed_at", "task"]