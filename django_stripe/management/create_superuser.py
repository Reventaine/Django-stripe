from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates a superuser with the given username and password'

    def handle(self, *args, **options):
        username = 'admin'
        password = 'admin'
        email = 'admin@example.com'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(f'Successfully created superuser "{username}"')
        else:
            self.stdout.write(f'Superuser "{username}" already exists')