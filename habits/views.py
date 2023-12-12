from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly

from habits.models import Habit
from habits.paginators import HabitsPaginator
from habits.serliazers import HabitSerializer
from users.permissions import UserIsStaff
from .tasks import schedule_reminder


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        related_habit = None
        new_habit = serializer.save(related_habit=related_habit, client=self.request.user)
        schedule_reminder.delay(new_habit.id)  # вызов отложенной задачи с передачей параметра

    # def perform_create(self, serializer):
    #     new_habit = serializer.save(related_habit=related_habit, client=self.request.user)
    #     new_habit.related_habit = self.request.user
    #     new_habit.seve()

    #     schedule_reminder.delay(new_habit.id)  # вызов отложенной задачи с передачей параметра


class HabitListAPIView(generics.ListAPIView):
    """Список публичных привычек"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    pagination_class = HabitsPaginator


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [UserIsStaff]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    queryset = Habit.objects.all()
    permission_classes = [UserIsStaff]


class UserHabitListAPIView(generics.ListAPIView):
    """Список привычек текущего пользователя с пагинацией"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitsPaginator

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)
