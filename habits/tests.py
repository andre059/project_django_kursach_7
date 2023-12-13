from users.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Habit


class HabitsHabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='sdk@mail.ru', password='zxc123zxc123', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place="test",
            time="2023-12-12T20:14:07.295779+03:00",
            action="бег",
            sign_pleasant_habit=True,
            periodicity=7,
            award="здоровье",
            time_to_execute=120,
            public=True
        )

    def test_create_habit(self):
        """Тестирование создание привычки"""

        response = self.client.post(
            path='/habit/create/',
            data={
                "place": "test",
                "time": "2023-12-13T19:34:20.134737+03:00",
                "action": "бег",
                "sign_pleasant_habit": True,
                "periodicity": 7,
                "award": "здоровье",
                "time_to_execute": 120,
                "public": True,
            }
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # print(response.json())

        self.assertEqual(
            response.json(),
            {
                "id": 2,
                "place": "test",
                "time": "2023-12-13T19:34:20.134737+03:00",
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

    def test_list_habit(self):
        """Тестирование публичных привычек"""

        response = self.client.get(path='/habit/')

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 1,
                        "place": "test",
                        "time": "2023-12-12T20:14:07.295779+03:00",
                        "action": "бег",
                        "sign_pleasant_habit": True,
                        "periodicity": 7,
                        "award": "здоровье",
                        "time_to_execute": 120,
                        "public": True,
                        "related_habit": None,
                        "client": None
                    }
                ]
            }
        )

    def test_update_habit(self):
        """Тестирование редактирование привычки"""

        data = {
            "place": "test2",
        }

        response = self.client.patch(
            f'/habit/update/{self.habit.id}/',
            data=data
        )

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # print(response)

        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "place": "test2",
                "time": "2023-12-12T20:14:07.295779+03:00",
                "action": "бег",
                "sign_pleasant_habit": True,
                "periodicity": 7,
                "award": "здоровье",
                "time_to_execute": 120,
                "public": True,
                "related_habit": None,
                "client": None
            }
        )

    def test_destroy_habit(self):
        """Тестирование удаление привычки"""

        response = self.client.delete(
            f'/habit/delete/{self.habit.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_user_list_habit(self):
        """Тестирование списка привычек текущего пользователя"""

        response = self.client.get(path='/habit/')

        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 1,
                        "place": "test",
                        "time": "2023-12-12T20:14:07.295779+03:00",
                        "action": "бег",
                        "sign_pleasant_habit": True,
                        "periodicity": 7,
                        "award": "здоровье",
                        "time_to_execute": 120,
                        "public": True,
                        "related_habit": None,
                        "client": None
                    }
                ]
            }
        )
