from typing import TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import AsyncGreenApi


class Receiving:
    def __init__(self, api: "AsyncGreenApi"):
        self.api = api

    async def receive_notification(self) -> Response:
        """
        The method is aimed for receiving one incoming notification
        from the notifications queue.

        https://green-api.com/en/docs/api/receiving/technology-http-api/ReceiveNotification/
        """
        return await self.api.request(
            "GET",
            "{{host}}/waInstance{{id_instance}}/receiveNotification/{{api_token_instance}}",
        )

    async def delete_notification(self, receipt_id: int) -> Response:
        """
        The method is aimed for deleting an incoming notification from
        the notification queue.

        https://green-api.com/en/docs/api/receiving/technology-http-api/DeleteNotification/
        """
        url = "{{host}}/waInstance{{id_instance}}/deleteNotification/{{api_token_instance}}"
        return await self.api.request("DELETE", f"{url}/{receipt_id}")

    async def download_file(self, chat_id: str, id_message: str) -> Response:
        """
        The method is aimed for downloading incoming and outgoing files.

        https://green-api.com/en/docs/api/receiving/files/DownloadFile/
        """
        request_body = {"chatId": chat_id, "idMessage": id_message}
        return await self.api.request(
            "POST",
            "{{host}}/waInstance{{id_instance}}/downloadFile/{{api_token_instance}}",
            request_body,
        )
