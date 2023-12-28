from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import AsyncGreenApi


class Marking:
    def __init__(self, api: "AsyncGreenApi"):
        self.api = api

    async def read_chat(self, chat_id: str, id_message: Optional[str] = None) -> Response:
        """
        The method is aimed for marking messages in a chat as read.

        https://green-api.com/en/docs/api/marks/ReadChat/
        """
        request_body = {"chatId": chat_id}
        if id_message is not None:
            request_body["idMessage"] = id_message

        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/readChat/{{api_token_instance}}",
            request_body,
        )
