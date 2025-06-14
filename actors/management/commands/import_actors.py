import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Name of the CSV file containing actor data to import.'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                birth_date = datetime.strptime(row['birth_date'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(f'Importing actor: {name}'))

                Actor.objects.update_or_create(
                    name=name,
                    birth_date=birth_date,
                    nationality=nationality,
                )

        self.stdout.write(self.style.SUCCESS(f'Successfully imported actors from {file_name}'))
