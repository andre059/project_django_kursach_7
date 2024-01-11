import os

from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='andrey01590@gmail.com',  # os.getenv('EMAIL_HOST_USER'),
            first_name='Admin',
            last_name='Adminich',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        user.set_password('viva416384352')  # os.getenv('CSU_SET_PASSWORD')
        user.save()
