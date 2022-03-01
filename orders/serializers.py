from rest_framework import serializers

from .models import Sandwich


class SandwichSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandwich
        fields = [
            "order_number",
            "type",
            "recipient",
            "completed"
        ]


class SandwichListSerializer(serializers.Serializer):
    sequence = serializers.IntegerField()
    schedule = serializers.CharField()
    type = serializers.CharField(required=False)
    task = serializers.CharField()
    order_number = serializers.IntegerField(required=False)
    recipient = serializers.CharField(required=False)
