from typing import TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import AsyncGreenApi


class Queues:
    def __init__(self, api: "AsyncGreenApi"):
        self.api = api

    async def show_messages_queue(self) -> Response:
        """
        The method is aimed for getting a list of messages in the queue
        to be sent.

        https://green-api.com/en/docs/api/queues/ShowMessagesQueue/
        """
        return await self.api.request(
            "GET",
            "{{host}}/waInstance{{id_instance}}/showMessagesQueue/{{api_token_instance}}",
        )

    async def clear_messages_queue(self) -> Response:
        """
        The method is aimed for clearing the queue of messages to be
        sent.

        https://green-api.com/en/docs/api/queues/ClearMessagesQueue/
        """
        return await self.api.request(
            "GET",
            "{{host}}/waInstance{{id_instance}}/clearMessagesQueue/{{api_token_instance}}",
        )
