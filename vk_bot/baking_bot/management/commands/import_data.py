import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from baking_bot.models import SimpleText, BakingType, Baking

Models = {
    SimpleText: 'commands.csv',
    BakingType: 'bakingtype.csv',
    Baking: 'baking.csv'
}


class Command(BaseCommand):
    help = 'Загрузка тестовых данных из csv файлов'

    def handle(self, *args, **options):
        for model, csv_files in Models.items():
            with open(
                f'{settings.BASE_DIR}/data_csv/{csv_files}',
                'r',
                encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                try:
                    model.objects.bulk_create(
                        model(**items) for items in reader
                    )
                except IntegrityError:
                    return 'Такие данные уже загружены в Базу'
        return (f'Данные успешно загружены.\n'
                f'Добавлены команды: '
                f'{[_.get("title") for _ in SimpleText.objects.values()]}'
                )
