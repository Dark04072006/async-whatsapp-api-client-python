import json
import logging
from typing import Any, Optional

from httpx import AsyncClient, Response

from .response import Response as GreenAPIResponse
from .tools import (
    account,
    device,
    groups,
    journals,
    marking,
    queues,
    receiving,
    sending,
    serviceMethods,
    webhooks
)


class AsyncGreenApi:
    host: str
    media: str
    id_instance: str
    api_token_instance: str

    def __init__(
            self,
            id_instance: str,
            api_token_instance: str,
            debug_mode: bool = False,
            raise_errors: bool = False,
            host: str = "https://api.green-api.com",
            media: str = "https://media.green-api.com"
    ):
        self.host = host
        self.media = media
        self.debug_mode = debug_mode
        self.raise_errors = raise_errors

        self.id_instance = id_instance
        self.api_token_instance = api_token_instance

        self.session = AsyncClient()
        self.account = account.Account(self)
        self.device = device.Device(self)
        self.groups = groups.Groups(self)
        self.journals = journals.Journals(self)
        self.marking = marking.Marking(self)
        self.queues = queues.Queues(self)
        self.receiving = receiving.Receiving(self)
        self.sending = sending.Sending(self)
        self.service_methods = serviceMethods.ServiceMethods(self)
        self.webhooks = webhooks.Webhooks(self)

        self.logger = logging.getLogger("whatsapp-api-client-python")
        self.__prepare_logger()

    async def request(
            self,
            method: str,
            url: str,
            payload: Optional[dict] = None,
            files: Optional[dict] = None
    ) -> GreenAPIResponse:
        url = url.replace("{{host}}", self.host)
        url = url.replace("{{media}}", self.media)
        url = url.replace("{{id_instance}}", self.id_instance)
        url = url.replace("{{api_token_instance}}", self.api_token_instance)

        try:
            if not files:
                response = await self.session.request(
                    method=method, url=url, json=payload
                )
            else:
                response = await self.session.request(
                    method=method, url=url, data=payload, files=files
                )
        except Exception as error:
            error_message = f"Request was failed with error: {error}."

            if self.raise_errors:
                raise GreenAPIError(error_message)
            self.logger.log(logging.CRITICAL, error_message)

            return GreenAPIResponse(None, error_message)

        await self.__handle_response(response)

        return GreenAPIResponse(response.status_code, response.text)

    async def raw_request(self, **arguments: Any) -> GreenAPIResponse:
        try:
            response = await self.session.request(**arguments)
        except Exception as error:
            error_message = f"Request was failed with error: {error}."

            if self.raise_errors:
                raise GreenAPIError(error_message)
            self.logger.log(logging.CRITICAL, error_message)

            return GreenAPIResponse(None, error_message)

        await self.__handle_response(response)

        return GreenAPIResponse(response.status_code, response.text)

    async def __handle_response(self, response: Response) -> None:
        status_code = response.status_code
        if status_code != 200 or self.debug_mode:
            try:
                data = json.dumps(
                    json.loads(response.text), ensure_ascii=False, indent=4
                )

            except json.decoder.JSONDecodeError:
                data = response.text

                if not data and status_code == 401:
                    data = "Unauthorized"

            if status_code != 200:
                error_message = (
                    f"Request was failed with status code: {status_code}."
                    f" Data: {data}"
                )

                if self.raise_errors:
                    raise GreenAPIError(error_message)
                self.logger.log(logging.ERROR, error_message)

                return None

            self.logger.log(
                logging.DEBUG, f"Request was successful with data: {data}"
            )

    def __prepare_logger(self) -> None:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            (
                "%(asctime)s:%(name)s:"
                "%(levelname)s:%(message)s"
            ), datefmt="%Y-%m-%d %H:%M:%S"
        ))

        self.logger.addHandler(handler)

        if not self.debug_mode:
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.DEBUG)


class AsyncGreenAPI(AsyncGreenApi):
    pass


class GreenAPIError(Exception):
    pass
