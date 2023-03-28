import csv
from django.core.management.base import BaseCommand
from ....food_compare.models import Question as Question_food_compare
from ....food_fact.models import Question as Question_food_fact
from ....food_labeler.models import Question as Question_food_labeler
from ....image_caption.models import Question as Question_image_caption
from ....sentiment.models import Question as Question_sentiment
from ....translation_validator.models import Question as Question_translation_validator

tables = {'food_compare': Question_food_compare,
          'food_fact': Question_food_fact,
          'food_labeler': Question_food_labeler,
          'image_caption': Question_image_caption,
          'sentiment': Question_sentiment,
          'translation_validator': Question_translation_validator,}

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('app', type=str, help='Indicates the name of the app')

    def handle(self, *args, **kwargs):
        app_name = kwargs['app']

        if app_name not in tables.keys():
            print('Invalid app name')
            return 

        with open(f'crowd_server/apps/{app_name}/data/{app_name}/data.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            header = next(reader)
            for i, line in enumerate(reader):
                params = dict(zip(header, line))
                table = tables[app_name]
                table.objects.create(**params)
