from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import AsyncGreenApi


class Journals:
    def __init__(self, api: "AsyncGreenApi"):
        self.api = api

    async def get_chat_history(self, chat_id: str, count: Optional[int] = None) -> Response:
        """
        The method returns the chat message history.

        https://green-api.com/en/docs/api/journals/GetChatHistory/
        """
        request_body = {"chatId": chat_id}
        if count is not None:
            request_body["count"] = count

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/getChatHistory/{{api_token_instance}}",
            request_body,
        )

    async def get_message(self, chat_id: str, id_message: str) -> Response:
        """
        The method returns the chat message.

        https://green-api.com/en/docs/api/journals/GetMessage/
        """
        request_body = {"chatId": chat_id, "idMessage": id_message}

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/getMessage/{{api_token_instance}}",
            request_body,
        )

    async def last_incoming_messages(self, minutes: Optional[int] = None) -> Response:
        """
        The method returns the last incoming messages of the account.

        https://green-api.com/en/docs/api/journals/LastIncomingMessages/
        """
        request_body = {"minutes": minutes} if minutes is not None else None

        return await self.api.request(
            "GET",
            "{{host}}/waInstance{{id_instance}}/lastIncomingMessages/{{api_token_instance}}",
            request_body,
        )

    async def last_outgoing_messages(self, minutes: Optional[int] = None) -> Response:
        """
        The method returns the last outgoing messages of the account.

        https://green-api.com/en/docs/api/journals/LastOutgoingMessages/
        """
        request_body = {"minutes": minutes} if minutes is not None else None

        return await self.api.request(
            "GET",
            "{{host}}/waInstance{{id_instance}}/lastOutgoingMessages/{{api_token_instance}}",
            request_body,
        )
