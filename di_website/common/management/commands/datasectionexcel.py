"""Management command that loads datasets."""


from django.core.management.base import BaseCommand

import pandas as pd
import numpy as np

from di_website.datasection.models import DataSource

class Command(BaseCommand):
    """Management command that that loads metadata from excel and creates new pages for datasection."""

    help = 'Import approved metadata from .xlsx file https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/edit#gid=1029209261'

    def handle(self, *args, **options):

        raw_data = 'https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/export?format=xlsx&id=1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU'

        source = pd.read_excel(raw_data, sheet_name='Source Data')
        dataset = pd.read_excel(raw_data, sheet_name='Dataset')
        figures = pd.read_excel(raw_data, sheet_name='Figures')

        skip = True
        for source_row in source.iterrows():
            if skip:
                skip = False
            else:
                source_dict = source_row[1].to_dict()
                source_check = DataSource.objects.filter(title=source_dict['Source title'])
                if not source_check:
                    new_source = DataSource(
                        title=source_dict['Source title'],
                        description=source_dict['Long description of the data source'],
                        organisation=source_dict['Organisation '],
                        link_to_metadata=source_dict['Link to the source'],
                        geography=source_dict['Geography information'],
                        link_to_data=source_dict['Link to the source']
                    )
                    new_source.save()

        skip = True
        for dataset_row in dataset.iterrows():
            if skip:
                skip = False
            else:
                dataset_dict = source_row[1].to_dict()
                import pdb; pdb.set_trace()


        self.stdout.write(self.style.SUCCESS('Called successfully'))
