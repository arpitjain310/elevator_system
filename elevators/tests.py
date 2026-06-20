from rest_framework import status
from rest_framework.test import APITestCase

from .models import Elevator, Request


class ElevatorSystemTests(APITestCase):
    def test_initialize_creates_the_requested_number_of_elevators(self):
        response = self.client.post(
            '/api/elevator-system/', {'number_of_elevators': 3}, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Elevator.objects.count(), 3)


class ElevatorActionTests(APITestCase):
    def setUp(self):
        self.elevator = Elevator.objects.create(current_floor=1)

    def test_save_request_stores_the_floor(self):
        url = f'/api/elevators/{self.elevator.pk}/save_request/'
        response = self.client.post(url, {'floor': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.elevator.requests.count(), 1)
        self.assertEqual(self.elevator.requests.first().floor, 5)

    def test_save_request_without_a_floor_is_rejected(self):
        url = f'/api/elevators/{self.elevator.pk}/save_request/'
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.elevator.requests.count(), 0)

    def test_next_destination_is_the_lowest_pending_floor(self):
        for floor in (5, 3, 8):
            req = Request.objects.create(floor=floor, direction='up')
            self.elevator.requests.add(req)
        url = f'/api/elevators/{self.elevator.pk}/next_destination/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['next_destination'], 3)

    def test_next_destination_defaults_to_current_floor_when_idle(self):
        url = f'/api/elevators/{self.elevator.pk}/next_destination/'
        response = self.client.get(url)
        self.assertEqual(response.data['next_destination'], self.elevator.current_floor)

    def test_doors_open_and_close(self):
        base = f'/api/elevators/{self.elevator.pk}'
        self.client.post(f'{base}/open_door/')
        self.elevator.refresh_from_db()
        self.assertTrue(self.elevator.is_door_open)

        self.client.post(f'{base}/close_door/')
        self.elevator.refresh_from_db()
        self.assertFalse(self.elevator.is_door_open)

    def test_mark_not_working_takes_the_elevator_offline(self):
        url = f'/api/elevators/{self.elevator.pk}/mark_not_working/'
        self.client.post(url)
        self.elevator.refresh_from_db()
        self.assertFalse(self.elevator.is_operational)
