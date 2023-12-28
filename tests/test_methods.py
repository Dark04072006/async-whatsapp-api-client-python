import asyncio
import typing
import unittest
from pathlib import Path
from unittest.mock import Mock, patch, AsyncMock

from async_whatsapp_api_client_python.API import AsyncGreenAPI
from async_whatsapp_api_client_python.response import Response

api = AsyncGreenAPI("", "")

BASE_DIR = Path(__file__).parent.parent

path = BASE_DIR / "examples/data/rates.png"


class MethodsTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_methods(self):
        with patch("httpx.AsyncClient.request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = AsyncMock(
                status_code=200, text=self.response_text,
            )

            methods = [
                *self.account_methods,
                *self.device_methods,
                *self.group_methods,
                *self.log_methods,
                *self.queue_methods,
                *self.read_mark_methods,
                *self.receiving_methods,
                *self.sending_methods,
                *self.service_methods
            ]

            responses = await asyncio.gather(*map(asyncio.create_task, methods))

            for response in responses:
                self.assertEqual(response.code, 200)
                self.assertEqual(response.data, {"example": {"key": "value"}})

            self.assertEqual(mock_request.call_count, len(methods))

    @property
    def response_text(self) -> str:
        return '{"example": {"key": "value"}}'

    @property
    def account_methods(self) -> typing.List[Response]:
        return [
            api.account.get_settings(),
            api.account.get_wa_settings(),
            api.account.set_settings({}),
            api.account.get_state_instance(),
            api.account.get_status_instance(),
            api.account.reboot(),
            api.account.logout(),
            api.account.qr(),
            api.account.set_profile_picture(path),
            api.account.get_authorization_code(0)
        ]

    @property
    def device_methods(self) -> typing.List[Response]:
        return [api.device.get_device_info()]

    @property
    def group_methods(self) -> typing.List[Response]:
        return [
            api.groups.create_group("", []),
            api.groups.update_group_name("", ""),
            api.groups.get_group_data(""),
            api.groups.add_group_participant("", ""),
            api.groups.remove_group_participant("", ""),
            api.groups.set_group_admin("", ""),
            api.groups.remove_admin("", ""),
            api.groups.set_group_picture("", path),
            api.groups.leave_group("")
        ]

    @property
    def log_methods(self) -> typing.List[Response]:
        return [
            api.journals.get_chat_history(""),
            api.journals.get_message("", ""),
            api.journals.last_incoming_messages(),
            api.journals.last_incoming_messages()
        ]

    @property
    def queue_methods(self) -> typing.List[Response]:
        return [
            api.queues.show_messages_queue(),
            api.queues.clear_messages_queue()
        ]

    @property
    def read_mark_methods(self) -> typing.List[Response]:
        return [api.marking.read_chat("")]

    @property
    def receiving_methods(self) -> typing.List[Response]:
        return [
            api.receiving.receive_notification(),
            api.receiving.delete_notification(0),
            api.receiving.download_file("", "")
        ]

    @property
    def sending_methods(self) -> typing.List[Response]:
        return [
            api.sending.send_message("", ""),
            api.sending.send_buttons("", "", []),
            api.sending.send_template_buttons("", "", []),
            api.sending.send_list_message("", "", "", []),
            api.sending.send_file_by_upload("", path),
            api.sending.send_file_by_url("", "", ""),
            api.sending.upload_file(path),
            api.sending.send_location("", 0.0, 0.0),
            api.sending.send_contact("", {}),
            api.sending.send_link("", ""),
            api.sending.forward_messages("", "", []),
            api.sending.send_poll("", "", [])
        ]

    @property
    def service_methods(self) -> typing.List[Response]:
        return [
            api.service_methods.check_whatsapp(0),
            api.service_methods.get_avatar(""),
            api.service_methods.get_contacts(),
            api.service_methods.get_contact_info(""),
            api.service_methods.delete_message("", ""),
            api.service_methods.archive_chat(""),
            api.service_methods.unarchive_chat(""),
            api.service_methods.set_disappearing_chat("")
        ]


if __name__ == '__main__':
    asyncio.run(unittest.main())
