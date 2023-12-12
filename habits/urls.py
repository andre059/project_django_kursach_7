from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitUpdateAPIView, HabitDestroyAPIView, \
    UserHabitListAPIView
from users.views import UserViewSet

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='create'),
    path('habit/', HabitListAPIView.as_view(), name='list'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete'),

    path('habit/', UserHabitListAPIView.as_view(), name='user-habit-list'),
] + router.urls
