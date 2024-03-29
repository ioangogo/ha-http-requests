"""Services that allow requests to be made from automations"""
import logging

import requests

from .const import basic_headers

DOMAIN = "http_requests"
_LOGGER = logging.getLogger(__name__)


def setup(hass, config):
    """Setup the component."""

    def http_get(call):
        """Performs a get request"""

        verify_ssl = (
            True if "verify_ssl" not in call.data.keys() else call.data["verify_ssl"]
        )

        headers = basic_headers
        if "headers" in call.data.keys():
            headers.update(call.data["headers"])

        auth = None
        if "auth_username" in call.data.keys() and "auth_password" in call.data.keys():
            auth = (
                call.data["auth_username"]
                if "auth_username" in call.data.keys()
                else None,
                call.data["auth_password"]
                if "auth_password" in call.data.keys()
                else None,
            )

        resp = requests.get(
            url=call.data["url"],
            params=call.data["get_params"]
            if "get_params" in call.data.keys()
            else None,
            headers=headers,
            verify=verify_ssl,
            timeout=10,
            auth=auth,
        )

        return resp.status_code == 200

    def http_post(call):
        """Performs a get request"""

        verify_ssl = (
            True if "verify_ssl" not in call.data.keys() else call.data["verify_ssl"]
        )

        headers = basic_headers
        if "headers" in call.data.keys():
            headers.update(call.data["headers"])

        auth = None
        if "auth_username" in call.data.keys() and "auth_password" in call.data.keys():
            auth = (
                call.data["auth_username"]
                if "auth_username" in call.data.keys()
                else None,
                call.data["auth_password"]
                if "auth_password" in call.data.keys()
                else None,
            )

        data = None

        if "data" in call.data.keys():
            data = call.data["data"]

        resp = requests.post(
            url=call.data["url"],
            data=data,
            headers=headers,
            verify=verify_ssl,
            timeout=10,
            auth=auth,
        )

        return resp.status_code == 200

    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, "http_get", http_get)
    hass.services.register(DOMAIN, "http_post", http_post)

    # Return boolean to indicate that initialization was successfully.
    return True
