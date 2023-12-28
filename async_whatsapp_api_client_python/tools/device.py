from typing import TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import AsyncGreenApi


class Device:
    def __init__(self, api: "AsyncGreenApi"):
        self.api = api

    async def get_device_info(self) -> Response:
        """
        The method is aimed for getting information about the device
        (phone) running WhatsApp Business application.

        https://green-api.com/en/docs/api/phone/GetDeviceInfo/
        """

        return await self.api.request(
            "GET", (
                "{{host}}/waInstance{{id_instance}}/"
                "getDeviceInfo/{{api_token_instance}}"
            )
        )
