import asyncio
import logging
from typing import Any, Callable, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..API import AsyncGreenApi


class Webhooks:
    _running: Optional[bool] = None

    def __init__(self, api: "AsyncGreenApi"):
        self.api = api

    @property
    def started(self) -> Optional[bool]:
        """Deprecated"""

        self.api.logger.log(logging.WARNING, "This property is deprecated.")

        return self._running

    @started.setter
    def started(self, value: bool) -> None:
        """Deprecated"""

        self.api.logger.log(logging.WARNING, "This property is deprecated.")

        self._running = value

    async def start_receiving_notifications(
            self, on_event: Callable[[str, dict], Any]
    ) -> None:
        self._running = True

        await self._start_polling(on_event)

    def stop_receiving_notifications(self) -> None:
        self._running = False

    async def job(self, on_event: Callable[[str, dict], Any]) -> None:
        """Deprecated"""

        self.api.logger.log(logging.WARNING, "This function is deprecated.")

        print(
            "Started receiving incoming notifications. "
            "To stop the process, press Ctrl + C."
        )

        while self.started:
            try:
                response = await self.api.receiving.receive_notification()
                if response.code == 200:
                    if not response.data:
                        continue
                    response = response.data

                    body = response["body"]
                    type_webhook = body["typeWebhook"]

                    on_event(type_webhook, body)

                    await self.api.receiving.delete_notification(
                        response["receiptId"]
                    )
            except KeyboardInterrupt:
                break

        print("Stopped receiving incoming notifications.")

    async def _start_polling(self, handler: Callable[[str, dict], Any]) -> None:
        self.api.session.headers["Connection"] = "keep-alive"

        self.api.logger.log(
            logging.INFO, "Started receiving incoming notifications."
        )

        while self._running:
            try:
                response = await self.api.receiving.receive_notification()
                if response.code == 200:
                    if not response.data:
                        continue
                    response = response.data

                    body = response["body"]
                    type_webhook = body["typeWebhook"]

                    handler(type_webhook, body)

                    await self.api.receiving.delete_notification(
                        response["receiptId"]
                    )
            except KeyboardInterrupt:
                break

        self.api.session.headers["Connection"] = "close"

        self.api.logger.log(
            logging.INFO, "Stopped receiving incoming notifications."
        )
