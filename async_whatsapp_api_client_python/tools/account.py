from pathlib import Path
from typing import Dict, TYPE_CHECKING, Union

from ..response import Response

if TYPE_CHECKING:
    from ..API import AsyncGreenApi


class Account:
    def __init__(self, api: "AsyncGreenApi"):
        self.api = api

    async def get_settings(self) -> Response:
        """
        The method is aimed for getting the current account settings.

        https://green-api.com/en/docs/api/account/GetSettings/
        """

        return await self.api.request(
            "GET", (
                "{{host}}/waInstance{{id_instance}}/"
                "getSettings/{{api_token_instance}}"
            )
        )

    async def get_wa_settings(self) -> Response:
        """
        The method is aimed to get information about the WhatsApp
        account.

        https://green-api.com/en/docs/api/account/GetWaSettings/
        """

        return await self.api.request(
            "GET", (
                "{{host}}/waInstance{{id_instance}}/"
                "getWaSettings/{{api_token_instance}}"
            )
        )

    async def set_settings(self, request_body: Dict[str, Union[int, str]]) -> Response:
        """
        The method is aimed for setting account settings.

        https://green-api.com/en/docs/api/account/SetSettings/
        """

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "setSettings/{{api_token_instance}}"
            ), request_body
        )

    async def get_state_instance(self) -> Response:
        """
        The method is aimed for getting the account state.

        https://green-api.com/en/docs/api/account/GetStateInstance/
        """

        return await self.api.request(
            "GET", (
                "{{host}}/waInstance{{id_instance}}/"
                "getStateInstance/{{api_token_instance}}"
            )
        )

    async def get_status_instance(self) -> Response:
        """
        The method is aimed for getting the status of the account
        instance socket connection with WhatsApp.

        https://green-api.com/en/docs/api/account/GetStatusInstance/
        """

        return await self.api.request(
            "GET", (
                "{{host}}/waInstance{{id_instance}}/"
                "getStatusInstance/{{api_token_instance}}"
            )
        )

    async def reboot(self) -> Response:
        """
        The method is aimed for rebooting an account.

        https://green-api.com/en/docs/api/account/Reboot/
        """

        return await self.api.request(
            "GET", (
                "{{host}}/waInstance{{id_instance}}/reboot/{{api_token_instance}}"
            )
        )

    async def logout(self) -> Response:
        """
        The method is aimed for logging out an account.

        https://green-api.com/en/docs/api/account/Logout/
        """

        return await self.api.request(
            "GET", (
                "{{host}}/waInstance{{id_instance}}/logout/{{api_token_instance}}"
            )
        )

    async def qr(self) -> Response:
        """
        The method is aimed for getting QR code.

        https://green-api.com/en/docs/api/account/QR/
        """

        return await self.api.request(
            "GET", "{{host}}/waInstance{{id_instance}}/qr/{{api_token_instance}}"
        )

    async def set_profile_picture(self, path: str) -> Response:
        """
        The method is aimed for setting an account picture.

        https://green-api.com/en/docs/api/account/SetProfilePicture/
        """

        file_name = Path(path).name
        files = {"file": (file_name, open(path, "rb"), "image/jpeg")}

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "setProfilePicture/{{api_token_instance}}"
            ), files=files
        )

    async def get_authorization_code(self, phone_number: int) -> Response:
        """
        The method is designed to authorize an instance by phone number.

        https://green-api.com/en/docs/api/account/GetAuthorizationCode/
        """

        request_body = {"phoneNumber": phone_number}

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "getAuthorizationCode/{{api_token_instance}}"
            ), request_body
        )
