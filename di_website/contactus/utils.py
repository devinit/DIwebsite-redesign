import requests
import os
from django.conf import settings
import json

END_POINT = 'https://api.hubapi.com/crm-objects/v1/objects/tickets?hapikey=' + \
    settings.HS_API_KEY


def create_new_ticket(payload):
    """
    Helper methods to help post forms to HubSpot CRM
    """

    try:
        data = json.dumps(payload)
        response = requests.post(
            END_POINT,
            headers={'Content-Type': 'application/json'},
            data=data)

        response.raise_for_status()
        # Check that response is 200, otherwise log failed posting
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred with hubspot: {http_err}')
    except Exception as err:

        # TODO Route to 500 error page from here

        print(f'Other error occurred with hubspot: {err}')
    else:
        pass
