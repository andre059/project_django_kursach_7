from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from users.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from .models import Habit


class HabitsHabitTestCase(APITestCase):

    def setUp(self) -> None:

        self.client = APIClient()
        self.user = User.objects.create_user(username='Андрей', email='sdk@mail.ru', password='zxc123zxc123')
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            {
                "place": "test",
                "time": "2023-12-12T20:14:07.295779+03:00",
                "action": "бег",
                "sign_pleasant_habit": True,
                "periodicity": 7,
                "award": "здоровье",
                "time_to_execute": 120,
                "public": True
            }
        )

    def test_create_habit(self):
        """Тестирование создание привычки"""

        # self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')  # Установка токена доступа
        response = self.client.post(path='/habit/create/, data={}')
            # '/habit/',
            # data=data,
            # format='json'  # Указание формата данных

        # response = self.client.post(
        #     '/habit/',
        #     data=data
        # )

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
