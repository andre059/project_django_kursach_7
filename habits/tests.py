from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


class HabitsHabitTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_habit(self):
        """Тестирование создание привычки"""

        data = {
            "place": "test",
            "time": "2023-12-12T20:14:07.295779+03:00",
            "action": "бег",
            "sign_pleasant_habit": True,
            "periodicity": 7,
            "award": "здоровье",
            "time_to_execute": 120,
            "public": True,
        }
        response = self.client.post(
            '/habit/',
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        print(response.json())

        self.assertEqual(
            response.json(),
            {
                "id": 28,
                "place": "test",
                "time": "2023-12-12T20:14:07.295779+03:00",
                "action": "бег",
                "sign_pleasant_habit": True,
                "periodicity": 7,
                "award": "здоровье",
                "time_to_execute": 120,
                "public": True,
                "related_habit": None,
                "client": 1
            }
        )
