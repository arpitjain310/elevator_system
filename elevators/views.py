from rest_framework import viewsets
from .models import Elevator
from .serializers import ElevatorSerializer

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
