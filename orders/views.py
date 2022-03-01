from rest_framework import viewsets, response
from .models import Sandwich
from .serializers import SandwichSerializer, SandwichListSerializer
from datetime import datetime, timedelta


class SandwichViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campaigns to be viewed or edited.
    """

    queryset = Sandwich.objects.all()
    serializer_class = SandwichSerializer


class OrderList(viewsets.ModelViewSet):
    """
    API endpoint that lists the uncompleted sandwich orders and their schedule.
    """
    queryset = Sandwich.objects.all().filter(completed=False).order_by('received_at')
    serializer_class = SandwichSerializer

    def list(self, request, **kwargs):
        data = self.get_queue()
        return response.Response(data)

    def get_queue(self):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        data = []
        seq = 1
        schedule = datetime.now().replace(hour=0, minute=0, second=0)
        for order in serializer.data:
            data.append({
                'sequence': seq,
                'schedule': schedule.strftime('%M:%S'),
                'type': order['type'],
                'task': 'Make Sandwich',
                'order_number': order['order_number'],
                'recipient': order['recipient'],
            })
            seq += 1
            schedule += timedelta(minutes=2, seconds=30)
            data.append({
                'sequence': seq,
                'schedule': schedule.strftime('%M:%S'),
                'type': order['type'],
                'task': 'Serve Sandwich',
                'order_number': order['order_number'],
                'recipient': order['recipient'],
            })
            seq += 1
            schedule += timedelta(minutes=1)
        data.append({
            'sequence': seq,
            'schedule': schedule.strftime('%M:%S'),
            'task': 'Take a Break',
        })
        serializer = SandwichListSerializer(data=data, many=True)
        serializer.is_valid()
        return serializer.data
