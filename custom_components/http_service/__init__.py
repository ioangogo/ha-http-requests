"""Example of a custom component exposing a service."""
import logging

import requests

from .const import (
    basic_headers
)

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "http_requests"
_LOGGER = logging.getLogger(__name__)



def Setup(hass, config):
    """Setup the service example component."""
    def http_get(call):
        """My first service."""
        if 'verify_ssl' not in call.data.keys():
            verify_ssl = basic_headers.update(call.data['verify_ssl'])
        else:
            verify_ssl = call.data['verify_ssl']

        if 'User-Agent' not in call.data['headers'].keys():
            headers = basic_headers
            headers.update(call.data['headers'])
        else:
            headers = call.data['headers']

        resp = requests.get(call.data['url'], param=call.data['get_params'], headers=headers, verify=verify_ssl)

        return resp.status_code == 200

    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, 'http_get', http_get)

    # Return boolean to indicate that initialization was successfully.
    return True
