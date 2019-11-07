"""Management command that loads datasets."""

import pandas as pd
import numpy as np
from datetime import datetime

from django.core.management.base import BaseCommand

from di_website.datasection.models import (
    DataSource,
    DatasetDownloads,
    FigurePageDownloads
)


class Command(BaseCommand):
    """Management command that that loads metadata from excel and creates new pages for datasection."""

    help = 'Import approved metadata from .xlsx file https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/edit#gid=1029209261'

    def handle(self, *args, **options):

        raw_data = 'https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/export?format=xlsx&id=1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU'

        source = pd.read_excel(raw_data, sheet_name='Source Data')
        dataset = pd.read_excel(raw_data, sheet_name='Dataset')
        figures = pd.read_excel(raw_data, sheet_name='Figures')

        # Data sources
        skip = True
        for source_row in source.iterrows():
            if skip:
                skip = False
            else:
                source_dict = source_row[1].to_dict()
                source_check = DataSource.objects.filter(title=source_dict['Source title'])
                if not source_check:

                    if type(source_dict['Date of access']) is not datetime:
                        try:
                            date_of_access = datetime.strptime(source_dict['Date of access'], "%d/%m/%Y")
                        except (ValueError, TypeError) as e:
                            date_of_access = None
                    else:
                        date_of_access = source_dict['Date of access']

                    tag_list = [tag.strip() for tag in source_dict['Keyword search'].split(",") if len(tag.strip()) < 100]
                    new_source = DataSource(
                        source_id=source_dict['Source ID'],
                        title=source_dict['Source title'],
                        organisation=source_dict['Organisation '],
                        description=source_dict['Long description of the data source'],
                        date_of_access=date_of_access,
                        link_to_data=source_dict['Link to the source'],
                        geography=source_dict['Geography information'],
                        internal_notes=source_dict['Internal notes'],
                        lead_analyst=source_dict['Analyst that worked on the data'],
                        license=source_dict['Licence']
                    )
                    new_source.topics.add(*tag_list)
                    new_source.save()

        # Datasets
        """
        (Pdb) dataset_dict.keys()
        dict_keys(['Dataset ID', 'What is the title of the data set?', 'What DI publication is this dataset associated with?', 'What is a long description of the data set?', 'Release date?', 'Geography information', 'Geographic coding', 'Unit', 'Keyword search', 'Internal notes', 'Analyst that worked on the data', 'Licence', 'Suggested citation', 'Source 1', 'Source 2 (optional)', 'Source 3 (optional)', 'Source 4 (optional)', 'Source 5 (optional)', 'Source 6 (optional)', 'Source 7 (optional)', 'Source 8 (optional)', 'Source 9 (optional)', 'Done', 'File location Excel', 'File name Excel', 'File location csv', 'File name csv', 'File notes', 'Signed-off and ready?'])
        """
        skip = True
        for dataset_row in dataset.iterrows():
            if skip:
                skip = False
            else:
                dataset_dict = dataset_row[1].to_dict()
                import pdb; pdb.set_trace()

        # Figures
        skip = True
        for figure_row in figures.iterrows():
            if skip:
                skip = False
            else:
                figure_dict = figure_row[1].to_dict()
                import pdb; pdb.set_trace()


        self.stdout.write(self.style.SUCCESS('Called successfully'))
