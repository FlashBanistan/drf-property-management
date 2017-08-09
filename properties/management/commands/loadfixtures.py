from django.core.management.base import BaseCommand, CommandError
from django.core import management
from django.core.management.commands import loaddata

class Command(BaseCommand):
    help = 'Loads fixture data'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        management.call_command('loaddata', 'authentication/fixtures/auth_data.json', verbosity=0)
        # self.stdout.write("Unterminated line", ending='')