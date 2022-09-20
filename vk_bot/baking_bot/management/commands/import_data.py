# from django.conf import settings
import os

from django.core.management.base import BaseCommand
# from baking_bot.models import SimpleText
from dotenv import load_dotenv

load_dotenv()
x = os.getenv('GROUP_ID')


class Command(BaseCommand):
    help = 'Тестирование данных'

    def handle(self, *args, **options):
        # return f'Info {SimpleText.objects.all()}'
        return f'Info check  ID -> {x}'
