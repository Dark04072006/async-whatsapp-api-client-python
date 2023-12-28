import mimetypes
import pathlib
from typing import Dict, List, Optional, TYPE_CHECKING, Union

from ..response import Response

if TYPE_CHECKING:
    from ..API import AsyncGreenApi


class Sending:
    def __init__(self, api: "AsyncGreenApi"):
        self.api = api

    async def send_message(
            self,
            chat_id: str,
            message: str,
            quoted_message_id: Optional[str] = None,
            archive_chat: Optional[bool] = None,
            link_preview: Optional[bool] = None,
    ) -> Response:
        """
        The method is aimed for sending a text message to a personal or
        a group chat.

        https://green-api.com/en/docs/api/sending/SendMessage/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/sendMessage/{{api_token_instance}}",
            request_body,
        )

    async def send_buttons(
            self,
            chat_id: str,
            message: str,
            buttons: List[Dict[str, Union[int, str]]],
            footer: Optional[str] = None,
            quoted_message_id: Optional[str] = None,
            archive_chat: Optional[bool] = None,
    ) -> Response:
        """
        The method is aimed for sending a button message to a personal
        or a group chat.

        https://green-api.com/en/docs/api/sending/SendButtons/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/sendButtons/{{api_token_instance}}",
            request_body,
        )

    async def send_template_buttons(
            self,
            chat_id: str,
            message: str,
            template_buttons: List[Dict[str, Union[int, Dict[str, str]]]],
            footer: Optional[str] = None,
            quoted_message_id: Optional[str] = None,
            archive_chat: Optional[bool] = None,
    ) -> Response:
        """
        The method is aimed for sending a message with template list
        interactive buttons to a personal or a group chat.

        https://green-api.com/en/docs/api/sending/SendTemplateButtons/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/sendTemplateButtons/{{api_token_instance}}",
            request_body,
        )

    async def send_list_message(
            self,
            chat_id: str,
            message: str,
            button_text: str,
            sections: List[Dict[str, Union[str, List[Dict[str, str]]]]],
            title: Optional[str] = None,
            footer: Optional[str] = None,
            quoted_message_id: Optional[str] = None,
            archive_chat: Optional[bool] = None,
    ) -> Response:
        """
        The method is aimed for sending a message with a select button
        from a list of values to a personal or a group chat.

        https://green-api.com/en/docs/api/sending/SendListMessage/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/sendListMessage/{{api_token_instance}}",
            request_body,
        )

    async def send_file_by_upload(
            self,
            chat_id: str,
            path: str,
            file_name: Optional[str] = None,
            caption: Optional[str] = None,
            quoted_message_id: Optional[str] = None,
    ) -> Response:
        """
        The method is aimed for sending a file uploaded by form
        (form-data).

        https://green-api.com/en/docs/api/sending/SendFileByUpload/
        """

        request_body = self.__handle_parameters(locals())

        file_name = pathlib.Path(path).name
        content_type = mimetypes.guess_type(file_name)[0]

        files = {"file": (file_name, open(path, "rb"), content_type)}

        request_body.pop("path")

        return await self.api.request(
            "POST",
            "{{media}}/waInstance{{id_instance}}/sendFileByUpload/{{api_token_instance}}",
            request_body,
            files,
        )

    async def send_file_by_url(
            self,
            chat_id: str,
            url_file: str,
            file_name: str,
            caption: Optional[str] = None,
            quoted_message_id: Optional[str] = None,
            archive_chat: Optional[bool] = None,
    ) -> Response:
        """
        The method is aimed for sending a file uploaded by URL.

        https://green-api.com/en/docs/api/sending/SendFileByUrl/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/sendFileByUrl/{{api_token_instance}}",
            request_body,
        )

    async def upload_file(self, path: str) -> Response:
        """
        The method is designed to upload a file to the cloud storage,
        which can be sent using the sendFileByUrl method.

        https://green-api.com/en/docs/api/sending/UploadFile/
        """

        file_name = pathlib.Path(path).name
        content_type = mimetypes.guess_type(file_name)[0]

        with open(path, "rb") as file:
            return await self.api.raw_request(
                method="POST",
                url=(
                    f"{self.api.media}/waInstance{self.api.id_instance}/"
                    f"uploadFile/{self.api.api_token_instance}"
                ),
                data=file.read(),
                headers={"Content-Type": content_type},
            )

    async def send_location(
            self,
            chat_id: str,
            latitude: float,
            longitude: float,
            name_location: Optional[str] = None,
            address: Optional[str] = None,
            quoted_message_id: Optional[str] = None,
    ) -> Response:
        """
        The method is aimed for sending location message.

        https://green-api.com/en/docs/api/sending/SendLocation/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/sendLocation/{{api_token_instance}}",
            request_body,
        )

    async def send_contact(
            self, chat_id: str, contact: Dict[str, Union[int, str]], quoted_message_id: Optional[str] = None
    ) -> Response:
        """
        The method is aimed for sending a contact message.

        https://green-api.com/en/docs/api/sending/SendContact/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/sendContact/{{api_token_instance}}",
            request_body,
        )

    async def send_link(
            self, chat_id: str, url_link: str, quoted_message_id: Optional[str] = None
    ) -> Response:
        """
        The method is deprecated. Please use SendMessage.

        The method is aimed for sending a message with a link, by which
        an image preview, title and description will be added.

        https://green-api.com/en/docs/api/sending/SendLink/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/sendLink/{{api_token_instance}}",
            request_body,
        )

    async def forward_messages(
            self, chat_id: str, chat_id_from: str, messages: List[str]
    ) -> Response:
        """
        The method is intended for forwarding messages to a personal or
        group chat.

        https://green-api.com/en/docs/api/sending/ForwardMessages/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/forwardMessages/{{api_token_instance}}",
            request_body,
        )

    async def send_poll(
            self,
            chat_id: str,
            message: str,
            options: List[Dict[str, str]],
            multiple_answers: Optional[bool] = None,
            quoted_message_id: Optional[str] = None,
    ) -> Response:
        """
        This method is intended for sending messages with a poll to a
        private or group chat.

        https://green-api.com/en/docs/api/sending/SendPoll/
        """

        request_body = self.__handle_parameters(locals())

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/sendPoll/{{api_token_instance}}",
            request_body,
        )

    @classmethod
    def __handle_parameters(cls, parameters: dict) -> dict:
        handled_parameters = {}

        if "self" in parameters:
            del parameters["self"]
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
