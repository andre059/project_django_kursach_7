from rest_framework import serializers

from habits.models import Habit
from habits.validators import TimetoexecuteValidator, RelatedHabitAwardValidator, \
    RelatedHabitSignpleasanthabitValidator, SignpleasanthabitHabitValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        default_validators = [TimetoexecuteValidator(), RelatedHabitAwardValidator(),
                              RelatedHabitSignpleasanthabitValidator(), SignpleasanthabitHabitValidator()]
