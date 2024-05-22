"""Example of a custom component exposing a service."""

from __future__ import annotations

import logging
import socket


from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "sendkeys_service"
_LOGGER = logging.getLogger(__name__)


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the sync service example component."""

    def sendkeys_service(call: ServiceCall) -> None:
        _LOGGER.debug("Received data %s", call.data)

        server_ip = call.data.get("serverIp")
        server_port = int(call.data.get("serverPort"))
        key_name = call.data.get("keyname")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Internet  # TCP

        try:
            sock.connect((server_ip, server_port))
            sock.send(key_name.encode())
        except (socket.error, socket.timeout):
            _LOGGER.debug("Send Failure.")
            sock.close()
            return False
        else:
            _LOGGER.debug("Message %s sent", key_name)
        finally:
            sock.close()

    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, "sendkeys", sendkeys_service)

    # Return boolean to indicate that initialization was successfully.
    return True
