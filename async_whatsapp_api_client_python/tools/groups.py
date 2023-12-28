from pathlib import Path
from typing import List, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import AsyncGreenApi


class Groups:
    def __init__(self, api: "AsyncGreenApi"):
        self.api = api

    async def create_group(self, group_name: str, chat_ids: List[str]) -> Response:
        """
        The method is aimed for creating a group chat.

        https://green-api.com/en/docs/api/groups/CreateGroup/
        """

        request_body = self.__handle_parameters({
            "groupName": group_name, "chatIds": chat_ids
        })

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "createGroup/{{api_token_instance}}"
            ), request_body
        )

    async def update_group_name(self, group_id: str, group_name: str) -> Response:
        """
        The method changes a group chat name.

        https://green-api.com/en/docs/api/groups/UpdateGroupName/
        """

        request_body = self.__handle_parameters({
            "groupId": group_id, "groupName": group_name
        })

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "updateGroupName/{{api_token_instance}}"
            ), request_body
        )

    async def get_group_data(self, group_id: str) -> Response:
        """
        The method gets group chat data.

        https://green-api.com/en/docs/api/groups/GetGroupData/
        """

        request_body = self.__handle_parameters({
            "groupId": group_id
        })

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "getGroupData/{{api_token_instance}}"
            ), request_body
        )

    async def add_group_participant(
            self, group_id: str, participant_chat_id: str
    ) -> Response:
        """
        The method adds a participant to a group chat.

        https://green-api.com/en/docs/api/groups/AddGroupParticipant/
        """

        request_body = self.__handle_parameters({
            "groupId": group_id, "participantChatId": participant_chat_id
        })

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "addGroupParticipant/{{api_token_instance}}"
            ), request_body
        )

    async def remove_group_participant(
            self, group_id: str, participant_chat_id: str
    ) -> Response:
        """
        The method removes a participant from a group chat.

        https://green-api.com/en/docs/api/groups/RemoveGroupParticipant/
        """

        request_body = self.__handle_parameters({
            "groupId": group_id, "participantChatId": participant_chat_id
        })

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "removeGroupParticipant/{{api_token_instance}}"
            ), request_body
        )

    async def set_group_admin(self, group_id: str, participant_chat_id: str) -> Response:
        """
        The method sets a group chat participant as an administrator.

        https://green-api.com/en/docs/api/groups/SetGroupAdmin/
        """

        request_body = self.__handle_parameters({
            "groupId": group_id, "participantChatId": participant_chat_id
        })

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "setGroupAdmin/{{api_token_instance}}"
            ), request_body
        )

    async def remove_admin(self, group_id: str, participant_chat_id: str) -> Response:
        """
        The method removes a participant from group chat administration
        rights.

        https://green-api.com/en/docs/api/groups/RemoveAdmin/
        """

        request_body = self.__handle_parameters({
            "groupId": group_id, "participantChatId": participant_chat_id
        })

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "removeAdmin/{{api_token_instance}}"
            ), request_body
        )

    async def set_group_picture(self, group_id: str, path: str) -> Response:
        """
        The method sets a group picture.

        https://green-api.com/en/docs/api/groups/SetGroupPicture/
        """

        request_body = self.__handle_parameters({"groupId": group_id})

        file_name = Path(path).name
        files = {"file": (file_name, open(path, "rb"), "image/jpeg")}

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "setGroupPicture/{{api_token_instance}}"
            ), request_body, files
        )

    async def leave_group(self, group_id: str) -> Response:
        """
        The method makes the current account user leave the group chat.

        https://green-api.com/en/docs/api/groups/LeaveGroup/
        """

        request_body = self.__handle_parameters({"groupId": group_id})

        return await self.api.request(
            "POST", (
                "{{host}}/waInstance{{id_instance}}/"
                "leaveGroup/{{api_token_instance}}"
            ), request_body
        )

    @classmethod
    def __handle_parameters(cls, parameters: dict) -> dict:
        handled_parameters = parameters.copy()

        if "self" in handled_parameters:
            del handled_parameters["self"]

        for key, value in parameters.items():
            if value is None:
                handled_parameters.pop(key)

        return handled_parameters
