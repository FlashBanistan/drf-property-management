from django.core.management.base import BaseCommand, CommandError
from django.core import management
from django.core.management.commands import loaddata

class Command(BaseCommand):
    help = 'Loads fixture data'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # Gotta manually setup clients in order for relations to work.
        # management.call_command('loaddata', 'clients/fixtures/client_data.json')
        management.call_command('loaddata', 'authentication/fixtures/auth_data.json')
        management.call_command('loaddata', 'properties/fixtures/property_data.json')
        management.call_command('loaddata', 'properties/fixtures/building_data.json')
        # management.call_command('loaddata', 'properties/fixtures/unit_data.json')
        # management.call_command('loaddata', 'tenants/fixtures/tenant_data.json')
