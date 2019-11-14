"""Management command that loads datasets."""

import os
from io import BytesIO
from datetime import datetime
import json
import requests
import csv

from boxsdk import JWTAuth, Client
from boxsdk.object.folder import Folder

from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings

from wagtail.documents.models import Document
from wagtail.core.models import Page

from di_website.home.models import HomePage
from di_website.ourteam.models import TeamMemberPage
from di_website.publications.inlines import (
    PublicationPageDataset, PublicationSummaryPageDataset,
    PublicationChapterPageDataset, PublicationAppendixPageDataset,
    LegacyPublicationPageDataset, ShortPublicationPageDataset
)
from di_website.datasection.models import (DataSectionPage, DataSetListing,
                                           DataSource, DatasetPage,
                                           DataSetSource, FigurePage,
                                           FigureSource, FigureDataSet,
                                           DatasetDownloads,
                                           FigurePageDownloads)


class Command(BaseCommand):
    """Management command that that loads metadata from CSV and creates new pages for datasection."""

    help = 'Import approved metadata from metadata file https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/edit#gid=1029209261'

    def handle(self, *args, **options):

        MISSING_VALUES = ["", " ", ".", "NA", "N/A", "N.A."]

        # Box Auth
        config = JWTAuth.from_settings_file(
            os.path.join(settings.BASE_DIR, 'box_config.json'))
        client = Client(config)

        def recurse_items(folder_items, box_items):
            for item in folder_items:
                if type(item) is Folder:
                    sub_folder_items = client.folder(
                        folder_id=item.id).get_items()
                    box_items = recurse_items(sub_folder_items, box_items)
                else:
                    box_items[item.name.lower()] = item.id
            return box_items

        box_items = {}
        folder_items = client.folder(folder_id="93089112686").get_items()
        box_items = recurse_items(folder_items, box_items)

        # Create IA if not already present
        dataset_listing = DataSetListing.objects.live().first()
        if not dataset_listing:
            data_section = DataSectionPage.objects.live().first()
            if not data_section:
                home_page = HomePage.objects.live().first()
                data_section = DataSectionPage(title="Data")
                home_page.add_child(instance=data_section)
                data_section.save_revision().publish()
            dataset_listing = DataSetListing(title="Datasets")
            data_section.add_child(instance=dataset_listing)
            dataset_listing.save_revision().publish()

        # Fetch data and parse
        source_csv_url = "https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/export?format=csv&id=1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU&gid=2086173829"
        dataset_csv_url = "https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/export?format=csv&id=1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU&gid=1736754230"
        figure_csv_url = "https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/export?format=csv&id=1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU&gid=1029209261"

        source_response = requests.get(source_csv_url)
        source_response.encoding = 'utf-8'
        source_text = source_response.iter_lines(decode_unicode=True)
        dataset_response = requests.get(dataset_csv_url)
        dataset_response.encoding = 'utf-8'
        dataset_text = dataset_response.iter_lines(decode_unicode=True)
        figure_response = requests.get(figure_csv_url)
        figure_response.encoding = 'utf-8'
        figure_text = figure_response.iter_lines(decode_unicode=True)

        # Data sources
        """
        (Pdb) source_dict.keys()
        dict_keys(['Source ID', 'Source title', 'Organisation ', 'Long description of the data source', 'Date of access', 'Link to the source', 'Geography information', 'Keyword search', 'Internal notes', 'Analyst that worked on the data', 'Licence', 'Check', 'Signed-off and ready?'])
        """
        skip = True
        source_reader = csv.DictReader(source_text)
        for source_dict in source_reader:
            if skip:
                skip = False
            else:
                source_check = DataSource.objects.filter(
                    source_id=source_dict['Source ID'])
                if not source_check and source_dict['Source title'] not in MISSING_VALUES and source_dict['Signed-off and ready?'].lower() == "yes":
                    print("source: ", source_dict['Source title'])
                    if type(source_dict['Date of access']) is not datetime:
                        try:
                            date_of_access = datetime.strptime(
                                source_dict['Date of access'], "%d/%m/%Y")
                        except (ValueError, TypeError) as e:
                            date_of_access = None
                    else:
                        date_of_access = source_dict['Date of access']

                    # try:
                    #     tag_list = [tag.strip() for tag in source_dict['Keyword search'].split(",") if len(tag.strip()) < 100 and len(tag.strip()) > 0]
                    # except AttributeError:
                    #     tag_list = []
                    new_source = DataSource(
                        source_id=source_dict['Source ID'],
                        title=source_dict['Source title'],
                        organisation=source_dict['Organisation '],
                        description=source_dict[
                            'Long description of the data source'],
                        date_of_access=date_of_access,
                        link_to_data=source_dict['Link to the source'],
                        geography=source_dict['Geography information'],
                        internal_notes=source_dict['Internal notes'],
                        licence=source_dict['Licence'])
                    # new_source.topics.add(*tag_list)

                    # Authors
                    author_names = source_dict[
                        'Analyst that worked on the data']
                    authors = []
                    if author_names not in MISSING_VALUES:
                        author_names_list = [author.strip() for author in author_names.split(",")]
                        for author_name in author_names_list:
                            internal_author_page_qs = TeamMemberPage.objects.filter(name=author_name)
                            if internal_author_page_qs:
                                author_obj = {"type": "internal_author", "value": internal_author_page_qs.first().pk}
                            else:
                                author_obj = {"type": "external_author", "value": {"name": author_name, "title": "", "photograph": None, "page": ""}}
                            authors.append(author_obj)
                    if authors:
                        new_source.authors = json.dumps(authors)
                    new_source.save()

        # Datasets
        """
        (Pdb) dataset_dict.keys()
        dict_keys(['Dataset ID', 'What is the title of the data set?', 'What DI publication is this dataset associated with?', 'What is a long description of the data set?', 'Release date?', 'Geography information', 'Geographic coding', 'Unit', 'Keyword search', 'Internal notes', 'Analyst that worked on the data', 'Licence', 'Suggested citation', 'Source 1', 'Source 2 (optional)', 'Source 3 (optional)', 'Source 4 (optional)', 'Source 5 (optional)', 'Source 6 (optional)', 'Source 7 (optional)', 'Source 8 (optional)', 'Source 9 (optional)', 'Done', 'File location Excel', 'File name Excel', 'File location csv', 'File name csv', 'File notes', 'Signed-off and ready?'])
        """
        source_keys = [
            'Source 1', 'Source 2 (optional)', 'Source 3 (optional)',
            'Source 4 (optional)', 'Source 5 (optional)',
            'Source 6 (optional)', 'Source 7 (optional)',
            'Source 8 (optional)', 'Source 9 (optional)'
        ]
        skip = True
        dataset_reader = csv.DictReader(dataset_text)
        for dataset_dict in dataset_reader:
            if skip:
                skip = False
            else:
                dataset_check = DatasetPage.objects.filter(
                    dataset_id=dataset_dict['Dataset ID'])
                if not dataset_check and dataset_dict[
                        'What is the title of the data set?'] not in MISSING_VALUES and dataset_dict['Signed-off and ready?'].lower() == "yes":
                    print("Dataset: ", dataset_dict[
                                'What is the title of the data set?'])
                    if type(dataset_dict['Release date?']) is not datetime:
                        try:
                            release_date = datetime.strptime(
                                dataset_dict['Release date?'], "%d/%m/%Y")
                        except (ValueError, TypeError) as e:
                            release_date = datetime.now()
                    else:
                        release_date = dataset_dict['Release date?']

                    meta_json = []
                    if dataset_dict[
                            'What is a long description of the data set?'] not in MISSING_VALUES:
                        meta_json.append({
                            "type":
                            "description",
                            "value":
                            dataset_dict[
                                'What is a long description of the data set?']
                        })
                    if dataset_dict['Geography information'] not in MISSING_VALUES:
                        meta_json.append({
                            "type":
                            "geography",
                            "value":
                            dataset_dict['Geography information']
                        })
                    if dataset_dict['Geographic coding'] not in MISSING_VALUES:
                        meta_json.append({
                            "type":
                            "geographic_coding",
                            "value":
                            dataset_dict['Geographic coding']
                        })
                    if dataset_dict['Unit'] not in MISSING_VALUES:
                        meta_json.append({
                            "type": "unit",
                            "value": dataset_dict['Unit']
                        })
                    if dataset_dict['Internal notes'] not in MISSING_VALUES:
                        meta_json.append({
                            "type":
                            "internal_notes",
                            "value":
                            dataset_dict['Internal notes']
                        })
                    if dataset_dict['Licence'] not in MISSING_VALUES:
                        meta_json.append({
                            "type": "licence",
                            "value": dataset_dict['Licence']
                        })
                    if dataset_dict['Suggested citation'] not in MISSING_VALUES:
                        meta_json.append({
                            "type":
                            "citation",
                            "value":
                            dataset_dict['Suggested citation']
                        })

                    new_dataset = DatasetPage(
                        title=dataset_dict[
                            'What is the title of the data set?'],
                        dataset_id=dataset_dict['Dataset ID'],
                        dataset_title=dataset_dict[
                            'What is the title of the data set?'],
                        release_date=release_date,
                        meta_data=json.dumps(meta_json))

                    # try:
                    #     tag_list = [tag.strip() for tag in dataset_dict['Keyword search'].split(",") if len(tag.strip()) < 100 and len(tag.strip()) > 0]
                    # except AttributeError:
                    #     tag_list = []
                    # new_dataset.topics.add(*tag_list)

                    dataset_listing.add_child(instance=new_dataset)

                    # Authors
                    author_names = dataset_dict[
                            'Analyst that worked on the data']
                    authors = []
                    if author_names not in MISSING_VALUES:
                        author_names_list = [author.strip() for author in author_names.split(",")]
                        for author_name in author_names_list:
                            internal_author_page_qs = TeamMemberPage.objects.filter(name=author_name)
                            if internal_author_page_qs:
                                author_obj = {"type": "internal_author", "value": internal_author_page_qs.first().pk}
                            else:
                                author_obj = {"type": "external_author", "value": {"name": author_name, "title": "", "photograph": None, "page": ""}}
                            authors.append(author_obj)
                    if authors:
                        new_dataset.authors = json.dumps(authors)

                    new_dataset.save_revision().publish()

                    if dataset_dict['What DI publication is this dataset associated with?'] not in MISSING_VALUES:
                        pub_check = Page.objects.filter(title=dataset_dict['What DI publication is this dataset associated with?']).live()
                        if pub_check:
                            pub_page = pub_check.first().specific()
                            if pub_page.verbose_name == "Publication Page":
                                PublicationPageDataset(item=pub_page, dataset=new_dataset).save()
                            elif pub_page.verbose_name == "Publication Summary Page":
                                PublicationSummaryPageDataset(item=pub_page, dataset=new_dataset).save()
                            elif pub_page.verbose_name == "Publication Chapter Page":
                                PublicationChapterPageDataset(item=pub_page, dataset=new_dataset).save()
                            elif pub_page.verbose_name == "Publication Appendix Page":
                                PublicationAppendixPageDataset(item=pub_page, dataset=new_dataset).save()
                            elif pub_page.verbose_name == "Legacy Publication Page":
                                LegacyPublicationPageDataset(item=pub_page, dataset=new_dataset).save()
                            elif pub_page.verbose_name == "Short Publication Page":
                                ShortPublicationPageDataset(item=pub_page, dataset=new_dataset).save()

                    for source_key in source_keys:
                        key_val = dataset_dict[source_key]
                        if key_val not in MISSING_VALUES:
                            try:
                                related_datasource = DataSource.objects.get(
                                    title=key_val)
                                DataSetSource(
                                    page=new_dataset,
                                    source=related_datasource).save()
                            except DataSource.DoesNotExist:
                                pass

                    if dataset_dict["File name Excel"] not in MISSING_VALUES:
                        item_name = dataset_dict["File name Excel"].lower(
                        ) + ".xlsx"
                        try:
                            item_id = box_items[item_name]
                            f = BytesIO()
                            client.file(item_id).download_to(f)
                            doc = Document(
                                title=dataset_dict["File name Excel"])
                            doc.file.save(item_name, File(f), save=True)
                            doc.save()
                            download = DatasetDownloads(
                                page=new_dataset,
                                title=dataset_dict["File name Excel"],
                                file=doc)
                            download.save()
                        except KeyError:
                            self.stdout.write(
                                self.style.WARNING(item_name + " not found."))

                    if dataset_dict["File name csv"] not in MISSING_VALUES:
                        item_name = dataset_dict["File name csv"].lower(
                        ) + ".csv"
                        try:
                            item_id = box_items[item_name]
                            f = BytesIO()
                            client.file(item_id).download_to(f)
                            doc = Document(title=dataset_dict["File name csv"])
                            doc.file.save(item_name, File(f), save=True)
                            doc.save()
                            download = DatasetDownloads(
                                page=new_dataset,
                                title=dataset_dict["File name csv"],
                                file=doc)
                            download.save()
                        except KeyError:
                            self.stdout.write(
                                self.style.WARNING(item_name + " not found."))

        # Figures
        """
        (Pdb) figure_dict.keys()
        dict_keys(['Chart ID', 'What is the descriptive title of the chart?', 'What is the active title used in the report', 'What is the Figure number used in the report', 'What report does the data set come from?', 'What is a long description of the chart data?', 'Release date', 'Geography information', 'Geography unit', 'Keyword search', 'Internal notes', 'Analyst that worked on the chart', 'Licence', 'Suggested citation', 'Source 1 (yellow = no source data [to check], orange = no source data [approved])', 'Source 2 (optional)', 'Source 3 (optional)', 'Source 4 (optional)', 'Source 5 (optional)', 'Source 6 (optional)', 'Source 7 (optional)', 'Source 8 (optional)', 'Source 9 (optional)', 'Source 10 (optional)', 'Source 11 (optional)', 'Source 12 (optional)', 'Source 13 (optional)', 'Source 14 (optional)', 'Source 15 (optional)', 'Dataset 1', 'Dataset 2', 'Dataset 3', 'Publication type', 'Done', 'File location', 'File name', 'Tab name', 'File notes', 'Signed-off and ready?'])
        """
        figure_source_keys = [
            'Source 1 (yellow = no source data [to check], orange = no source data [approved])',
            'Source 2 (optional)', 'Source 3 (optional)',
            'Source 4 (optional)', 'Source 5 (optional)',
            'Source 6 (optional)', 'Source 7 (optional)',
            'Source 8 (optional)', 'Source 9 (optional)',
            'Source 10 (optional)', 'Source 11 (optional)',
            'Source 12 (optional)', 'Source 13 (optional)',
            'Source 14 (optional)', 'Source 15 (optional)'
        ]
        figure_dataset_keys = ['Dataset 1', 'Dataset 2', 'Dataset 3']
        skip = True
        figure_reader = csv.DictReader(figure_text)
        for figure_dict in figure_reader:
            if skip:
                skip = False
            else:
                figure_check = FigurePage.objects.filter(
                    figure_id=figure_dict['Chart ID'])
                if not figure_check and figure_dict[
                        'What is the descriptive title of the chart?'] not in MISSING_VALUES and figure_dict['Signed-off and ready?'].lower() == "yes":
                    print("Figure: ", figure_dict[
                                'What is the descriptive title of the chart?'])
                    if type(figure_dict['Release date']) is not datetime:
                        try:
                            release_date = datetime.strptime(
                                figure_dict['Release date'], "%d/%m/%Y")
                        except (ValueError, TypeError) as e:
                            release_date = datetime.now()
                    else:
                        release_date = figure_dict['Release date']

                    meta_json = []
                    if figure_dict[
                            'What is a long description of the chart data?'] not in MISSING_VALUES:
                        meta_json.append({
                            "type":
                            "description",
                            "value":
                            figure_dict[
                                'What is a long description of the chart data?']
                        })
                    if figure_dict['Geography information'] not in MISSING_VALUES:
                        meta_json.append({
                            "type":
                            "geography",
                            "value":
                            figure_dict['Geography information']
                        })
                    if figure_dict['Geography unit'] not in MISSING_VALUES:
                        meta_json.append({
                            "type": "geographic_coding",
                            "value": figure_dict['Geography unit']
                        })
                    if figure_dict['Internal notes'] not in MISSING_VALUES:
                        meta_json.append({
                            "type": "internal_notes",
                            "value": figure_dict['Internal notes']
                        })
                    if figure_dict['Licence'] not in MISSING_VALUES:
                        meta_json.append({
                            "type": "licence",
                            "value": figure_dict['Licence']
                        })
                    if figure_dict['Suggested citation'] not in MISSING_VALUES:
                        meta_json.append({
                            "type":
                            "citation",
                            "value":
                            figure_dict['Suggested citation']
                        })
                    if figure_dict[
                        'What report does the data set come from?'] not in MISSING_VALUES:
                        pub_check = Page.objects.filter(title=figure_dict[
                            'What report does the data set come from?']).live()
                        if pub_check:
                            pub_page = pub_check.first()

                    new_figure = FigurePage(
                        title=figure_dict[
                            'What is the descriptive title of the chart?'],
                        figure_id=figure_dict['Chart ID'],
                        name=figure_dict[
                            'What is the active title used in the report'],
                        figure_title=figure_dict[
                            'What is the descriptive title of the chart?'],
                        release_date=release_date,
                        publication=pub_page,
                        meta_data=json.dumps(meta_json))

                    # try:
                    #     tag_list = [tag.strip() for tag in figure_dict['Keyword search'].split(",") if len(tag.strip()) < 100 and len(tag.strip()) > 0]
                    # except AttributeError:
                    #     tag_list = []
                    # new_figure.topics.add(*tag_list)

                    dataset_listing.add_child(instance=new_figure)

                    # Authors
                    author_names = figure_dict[
                            'Analyst that worked on the chart']
                    authors = []
                    if author_names not in MISSING_VALUES:
                        author_names_list = [author.strip() for author in author_names.split(",")]
                        for author_name in author_names_list:
                            internal_author_page_qs = TeamMemberPage.objects.filter(name=author_name)
                            if internal_author_page_qs:
                                author_obj = {"type": "internal_author", "value": internal_author_page_qs.first().pk}
                            else:
                                author_obj = {"type": "external_author", "value": {"name": author_name, "title": "", "photograph": None, "page": ""}}
                            authors.append(author_obj)
                    if authors:
                        new_figure.authors = json.dumps(authors)

                    new_figure.save_revision().publish()

                    for source_key in figure_source_keys:
                        key_val = figure_dict[source_key]
                        if key_val not in MISSING_VALUES:
                            try:
                                related_datasource = DataSource.objects.get(
                                    title=key_val)
                                FigureSource(page=new_figure,
                                             source=related_datasource).save()
                            except DataSource.DoesNotExist:
                                pass

                    for dataset_key in figure_dataset_keys:
                        key_val = figure_dict[dataset_key]
                        if key_val not in MISSING_VALUES:
                            try:
                                related_dataset = DatasetPage.objects.get(
                                    title=key_val)
                                FigureDataSet(page=new_figure,
                                              dataset=related_dataset).save()
                            except DatasetPage.DoesNotExist:
                                pass

                    if figure_dict["File name"] not in MISSING_VALUES:
                        item_name = figure_dict["File name"].lower() + ".csv"
                        try:
                            item_id = box_items[item_name]
                            f = BytesIO()
                            client.file(item_id).download_to(f)
                            doc = Document(title=figure_dict["File name"])
                            doc.file.save(item_name, File(f), save=True)
                            doc.save()
                            download = FigurePageDownloads(
                                page=new_figure,
                                title=figure_dict["File name"],
                                file=doc)
                            download.save()
                        except KeyError:
                            pass

                        item_name = figure_dict["File name"].lower() + ".xlsx"
                        try:
                            item_id = box_items[item_name]
                            f = BytesIO()
                            client.file(item_id).download_to(f)
                            doc = Document(title=figure_dict["File name"])
                            doc.file.save(item_name, File(f), save=True)
                            doc.save()
                            download = FigurePageDownloads(
                                page=new_figure,
                                title=figure_dict["File name"],
                                file=doc)
                            download.save()
                        except KeyError:
                            self.stdout.write(
                                self.style.WARNING(item_name + " not found."))

        self.stdout.write(self.style.SUCCESS('Called successfully'))
