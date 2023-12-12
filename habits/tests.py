from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


class HabitsHabitTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_habit(self):
        """Тестирование создание привычки"""

        data = {
            "place": "Test",
            "time": 100,
            "action": "пробежка",
            "sign_pleasant_habit": "True",
            "periodicity": 1,
            "award": "класс",
            "time_to_execute": "120",
            "public": "None"
        }
        response = self.client.post(
            '/habit/',
            data=data
        )

        print(response)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
