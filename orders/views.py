from rest_framework import viewsets
from .models import Sandwich
from .serializers import SandwichSerializer


class SandwichViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campaigns to be viewed or edited.
    """

    queryset = Sandwich.objects.all()
    serializer_class = SandwichSerializer
