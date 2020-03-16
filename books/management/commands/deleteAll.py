from datetime import datetime
from django.core.management.base import BaseCommand, CommandError

from books.models import Author


class Command(BaseCommand):
    help = 'Deletes the old database'

    def handle(self, *args, **options):
        try:
            Author.objects.all().delete()
        except:
            # error message
            raise CommandError('error job not completed')

        # success message
        self.stdout.write('Successfully removed all old authors')
