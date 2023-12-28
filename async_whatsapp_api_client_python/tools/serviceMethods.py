from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import AsyncGreenApi


class ServiceMethods:
    def __init__(self, api: "AsyncGreenApi"):
        self.api = api

    async def check_whatsapp(self, phone_number: int) -> Response:
        """
        The method checks WhatsApp account availability on a phone
        number.

        https://green-api.com/en/docs/api/service/CheckWhatsapp/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/checkWhatsapp/{{api_token_instance}}",
            request_body,
        )

    async def get_avatar(self, chat_id: str) -> Response:
        """
        The method returns a user or a group chat avatar.

        https://green-api.com/en/docs/api/service/GetAvatar/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/getAvatar/{{api_token_instance}}",
            request_body,
        )

    async def get_contacts(self) -> Response:
        """
        The method is aimed for getting a list of the current account
        contacts.

        https://green-api.com/en/docs/api/service/GetContacts/
        """

        return await self.api.request(
            "GET",
            "{{host}}/waInstance{{id_instance}}/getContacts/{{api_token_instance}}",
        )

    async def get_contact_info(self, chat_id: str) -> Response:
        """
        The method is aimed for getting information on a contact.

        https://green-api.com/en/docs/api/service/GetContactInfo/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/getContactInfo/{{api_token_instance}}",
            request_body,
        )

    async def delete_message(self, chat_id: str, id_message: str) -> Response:
        """
        The method deletes a message from a chat.

        https://green-api.com/en/docs/api/service/deleteMessage/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/deleteMessage/{{api_token_instance}}",
            request_body,
        )

    async def archive_chat(self, chat_id: str) -> Response:
        """
        The method archives a chat.

        https://green-api.com/en/docs/api/service/archiveChat/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/archiveChat/{{api_token_instance}}",
            request_body,
        )

    async def unarchive_chat(self, chat_id: str) -> Response:
        """
        The method unarchives a chat.

        https://green-api.com/en/docs/api/service/unarchiveChat/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/unarchiveChat/{{api_token_instance}}",
            request_body,
        )

    async def set_disappearing_chat(
            self, chat_id: str, ephemeral_expiration: Optional[int] = None
    ) -> Response:
        """
        The method is aimed for changing settings of disappearing
        messages in chats.

        https://green-api.com/en/docs/api/service/SetDisappearingChat/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/setDisappearingChat/{{api_token_instance}}",
            request_body,
        )

    @classmethod
    def __handle_parameters(cls, parameters: dict) -> dict:
        handled_parameters = {}

        for key, value in parameters.items():
            if value is not None:
                camel_case_key = cls.__snake_to_camel_case(key)
                handled_parameters[camel_case_key] = value

        return handled_parameters

    @staticmethod
    def __snake_to_camel_case(snake_case_str: str) -> str:
        # Convert snake_case to camelCase
        components = snake_case_str.split('_')
        camel_case_str = components[0] + ''.join(x.title() for x in components[1:])
        return camel_case_str
