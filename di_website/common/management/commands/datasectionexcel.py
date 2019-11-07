"""Management command that loads datasets."""

import pandas as pd
import numpy as np
from datetime import datetime
import json

from django.core.management.base import BaseCommand

from di_website.home.models import HomePage
from di_website.datasection.models import (
    DataSectionPage,
    DataSetListing,
    DataSource,
    DatasetPage,
    DataSetSource,
    DatasetDownloads,
    FigurePageDownloads
)


class Command(BaseCommand):
    """Management command that that loads metadata from excel and creates new pages for datasection."""

    help = 'Import approved metadata from .xlsx file https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/edit#gid=1029209261'

    def handle(self, *args, **options):

        # Create IA if not already present
        dataset_listing = DataSetListing.objects.live().first()
        if not dataset_listing:
            data_section = DataSectionPage.objects.live().first()
            if not data_section:
                home_page = HomePage.objects.live().first()
                data_section = DataSectionPage(
                    title="Data"
                )
                home_page.add_child(instance=data_section)
                data_section.save_revision().publish()
            dataset_listing = DataSetListing(
                title="Datasets"
            )
            data_section.add_child(instance=dataset_listing)
            dataset_listing.save_revision().publish()

        # Fetch data and parse
        raw_data = 'https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/export?format=xlsx&id=1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU'

        source = pd.read_excel(raw_data, sheet_name='Source Data')
        dataset = pd.read_excel(raw_data, sheet_name='Dataset')
        figures = pd.read_excel(raw_data, sheet_name='Figures')

        # Data sources
        """
        (Pdb) source_dict.keys()
        dict_keys(['Source ID', 'Source title', 'Organisation ', 'Long description of the data source', 'Date of access', 'Link to the source', 'Geography information', 'Keyword search', 'Internal notes', 'Analyst that worked on the data', 'Licence', 'Check', 'Signed-off and ready?'])
        """
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

                    try:
                        tag_list = [tag.strip() for tag in source_dict['Keyword search'].split(",") if len(tag.strip()) < 100]
                    except AttributeError:
                        tag_list = []
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
        source_keys = [
            'Source 1',
            'Source 2 (optional)',
            'Source 3 (optional)',
            'Source 4 (optional)',
            'Source 5 (optional)',
            'Source 6 (optional)',
            'Source 7 (optional)',
            'Source 8 (optional)',
            'Source 9 (optional)'
        ]
        skip = True
        for dataset_row in dataset.iterrows():
            if skip:
                skip = False
            else:
                dataset_dict = dataset_row[1].to_dict()
                dataset_check = DataSource.objects.filter(title=dataset_dict['Dataset ID'])
                if not dataset_check:
                    if type(dataset_dict['Release date?']) is not datetime:
                        try:
                            release_date = datetime.strptime(dataset_dict['Release date?'], "%d/%m/%Y")
                        except (ValueError, TypeError) as e:
                            release_date = None
                    else:
                        release_date = dataset_dict['Release date?']

                    meta_json = []
                    if dataset_dict['What is a long description of the data set?'] is not np.nan:
                        meta_json.append({"type": "description", "value": dataset_dict['What is a long description of the data set?']})
                    if dataset_dict['Geography information'] is not np.nan:
                        meta_json.append({"type": "geography", "value": dataset_dict['Geography information']})
                    if dataset_dict['Geographic coding'] is not np.nan:
                        meta_json.append({"type": "geographic_coding", "value": dataset_dict['Geographic coding']})
                    if dataset_dict['Unit'] is not np.nan:
                        meta_json.append({"type": "unit", "value": dataset_dict['Unit']})
                    if dataset_dict[''] is not np.nan:
                        meta_json.append({"type": "internal_notes", "value": dataset_dict['Internal notes']})
                    if dataset_dict[''] is not np.nan:
                        meta_json.append({"type": "lead_analyst", "value": dataset_dict['Analyst that worked on the data']})
                    if dataset_dict[''] is not np.nan:
                        meta_json.append({"type": "license", "value": dataset_dict['Licence']})
                    if dataset_dict[''] is not np.nan:
                        meta_json.append({"type": "citation", "value": dataset_dict['Suggested citation']})

                    new_dataset = DatasetPage(
                        title=dataset_dict['What is the title of the data set?'],
                        dataset_id=dataset_dict['Dataset ID'],
                        dataset_title=dataset_dict['What is the title of the data set?'],
                        release_date=release_date,
                        meta_data=json.dumps(meta_json)
                    )
                    dataset_listing.add_child(instance=new_dataset)
                    new_dataset.save_revision().publish()

                    for source_key in source_keys:
                        key_val = dataset_dict[source_key]
                        if key_val is not np.nan:
                            try:
                                related_datasource = DataSource.objects.get(title=key_val)
                                DataSetSource(
                                    page=new_dataset,
                                    source=related_datasource
                                ).save()
                            except DataSource.DoesNotExist:
                                pass

                    # TODO: Take XLSX and CSV links, format as box, download them, create BaseDownload items, attach to page model

        # Figures
        skip = True
        for figure_row in figures.iterrows():
            if skip:
                skip = False
            else:
                figure_dict = figure_row[1].to_dict()
                import pdb; pdb.set_trace()


        self.stdout.write(self.style.SUCCESS('Called successfully'))
