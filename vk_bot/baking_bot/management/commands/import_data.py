# from django.conf import settings
from django.core.management.base import BaseCommand
# from baking_bot.models import SimpleText


class Command(BaseCommand):
    help = 'Тестирование данных'

    def handle(self, *args, **options):
        # return f'Info {SimpleText.objects.all()}'
        return f'Info check, {x}'
