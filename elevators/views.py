from rest_framework import viewsets
from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ElevatorSystemViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['POST'])
    def initialize(self, request):
        number_of_elevators = request.data.get('number_of_elevators', 1)
        self.create_elevators(number_of_elevators)

        return Response({'message': f'Elevator system initialized with {number_of_elevators} elevators'})

    def create_elevators(self, number_of_elevators):
        for _ in range(number_of_elevators):
            Elevator.objects.create()


class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=True, methods=['GET'])
    def requests(self, request, pk=None):
        elevator = self.get_object()
        requests = elevator.requests.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    def calculate_next_destination(self, elevator):

        if elevator.requests.exists():
            closest_request = elevator.requests.order_by('floor').first()
            return closest_request.floor

        return elevator.current_floor

    @action(detail=True, methods=['GET'])
    def next_destination(self, request, pk=None):
        elevator = self.get_object()
        next_floor = self.calculate_next_destination(elevator)

        return Response({'next_destination': next_floor})

    @action(detail=True, methods=['GET'])
    def is_moving_up(self, request, pk=None):
        elevator = self.get_object()
        return Response({'is_moving_up': elevator.is_moving})

    @action(detail=True, methods=['POST'])
    def save_request(self, request, pk=None):
        elevator = self.get_object()
        floor = request.data.get('floor')
        direction = 'up' if floor > elevator.current_floor else 'down' if floor < elevator.current_floor else 'none'
        new_request = Request.objects.create(floor=floor, direction=direction)
        elevator.requests.add(new_request)
        elevator.save()
        return Response({'message': 'Request saved successfully'})

    @action(detail=True, methods=['POST'])
    def mark_not_working(self, request, pk=None):
        elevator = self.get_object()
        elevator.is_operational = False
        elevator.save()
        return Response({'message': 'Elevator marked as not working'})

    @action(detail=True, methods=['POST'])
    def open_door(self, request, pk=None):
        elevator = self.get_object()
        elevator.is_door_open = True
        elevator.save()
        return Response({'message': 'Door opened'})

    @action(detail=True, methods=['POST'])
    def close_door(self, request, pk=None):
        elevator = self.get_object()
        elevator.is_door_open = False
        elevator.save()
        return Response({'message': 'Door closed'})
