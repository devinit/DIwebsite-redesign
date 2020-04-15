import csv

from django.core.management.base import BaseCommand

from di_website.spotlight.models import SpotlightIndicator


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.update_indicators_from_concept('spotlight-uganda-concept.csv')
        self.update_indicators_from_concept('spotlight-kenya-concept.csv')

    def update_indicators_from_concept(self, file_name):
        try:
            with open(file_name, 'rt') as my_file:
                reader = csv.reader(my_file)
                count = 0
                for row in reader:
                    if count != 0:
                        ddw_id = row[0]
                        source = row[14]
                        self.update_indicator(ddw_id, source)
                    count += 1
            print('Indicators successfully updated')
        except FileNotFoundError:
            print('No import of ' + file_name + ' indicator data done. File "' + file_name + '" not found')


    def update_indicator(self, ddw_id, source):
        indicators = SpotlightIndicator.objects.filter(ddw_id=ddw_id)
        indicator = indicators[0] if indicators else None
        if indicator:
            indicator.source = source
            indicator.save_revision().publish()
