
import getpass
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a super admin if missing."

    def add_arguments(self, parser):
        parser.add_argument("--username", default="admin")

    def _ask_password(self):
        return getpass.getpass("Password: ")

    def handle(self, *args, **options):
        User = get_user_model()
        name = options["username"]
        if User.objects.filter(username=name).exists():
            self.stdout.write("skipped")
            return
        User.objects.create_superuser(
            username=name,
            password=self._ask_password(),
        )
        self.stdout.write(self.style.SUCCESS(f"Super admin '{name}' created"))