from celery import shared_task
from datetime import datetime, timedelta

from django.core.management import call_command

from habits.models import Habit
from users.management.commands.testn import Command


@shared_task
def schedule_reminder(habit_id):
    """Отложенная задача"""

    habit = Habit.objects.get(id=habit_id)

    if not habit.sign_pleasant_habit and habit.time <= datetime.now() - timedelta(days=7):
        if (datetime.now() - habit.time).days > 7:
            habit.sign_pleasant_habit = True
            habit.save()
            call_command('command')

    # habitude = Habit.objects.filter(sign_pleasant_habit=False, time__lte=datetime.now() - timedelta(days=7))
    # for habit in habitude:
    #     if (datetime.now() - habit.time).days > 7:
    #         habit.sign_pleasant_habit = True
    #         habit.save()
    #         call_command('command')


            # Command.call_command('apply_async')

    # Command.apply_async(countdown=7*24*60*60)

    # habitude = Habit.objects.all()
    # for habit in habitude:
    #     created_at = habit.time
    #     if not habit.sign_pleasant_habit and created_at + timedelta(days=7) < datetime.now():