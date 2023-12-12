from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.paginators import HabitsPaginator
from users.models import User
from users.permissions import UserIsStaff
from users.serliazers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """класс для вывода списка и информации по одному объекту"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    pagination_class = HabitsPaginator
