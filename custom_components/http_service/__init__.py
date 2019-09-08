"""Example of a custom component exposing a service."""
import asyncio
import logging

from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "http_service"
_LOGGER = logging.getLogger(__name__)


@asyncio.coroutine
def async_setup(hass, config):
    """Setup the service example component."""
    @callback
    def http_request(call):
        """My first service."""
        _LOGGER.info('Received data', call.data)

    # Register our service with Home Assistant.
    hass.services.async_register(DOMAIN, 'demo', my_service)

    # Return boolean to indicate that initialization was successfully.
    return True
