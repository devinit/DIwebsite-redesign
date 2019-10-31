"""Management command that fixes imported WP content."""

import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from di_website.ourteam.models import TeamMemberPage

import requests
import pandas as pd
import numpy as np


class Command(BaseCommand):
    """Management command that that loads metadata from excel and creates new pages for datasection."""

    help = 'Import approved metadata from .xlsx file https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/edit#gid=1029209261'

    def handle(self, *args, **options):

        raw_data = 'https://docs.google.com/spreadsheets/d/1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU/export?format=xlsx&id=1pDbdncnm1TF41kJJX2WjZ2Wq9juOvUqU'

        dataset = pd.read_excel(raw_data, sheet_name='Dataset')
        source = pd.read_excel(raw_data, sheet_name='Source Data')
        figures = pd.read_excel(raw_data, sheet_name='Figures')

        self.stdout.write(self.style.SUCCESS('Called successfully'))
