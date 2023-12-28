# async-whatsapp-api-client-python

async-whatsapp-api-client-python is an asynchronous library for integration with WhatsApp messenger using the API
service [green-api.com](https://green-api.com/en/). You should get a registration token and an account ID in
your [personal cabinet](https://console.green-api.com/) to use the library. There is a free developer account tariff.

## Installation

Dear users,

We apologize for any inconvenience, but currently, PyPI (Python Package Index) registration is temporarily disabled due
to technical issues. This restriction has been imposed by PyPI, and we are working closely with their team to resolve
this issue as soon as possible.

**How it affects you:**

At the moment, you cannot install our project using the standard `pip install` command via PyPI. However, we have
provided an alternative installation method through TestPyPI. You can install the project as follows:

```shell
pip install -i https://test.pypi.org/simple/ async-whatsapp-api-client-python
```

## Import

```python
from async_whatsapp_api_client_python import API
```

## Examples

### How to initialize an object

```python
from async_whatsapp_api_client_python import API

async_green_api = API.AsyncGreenApi(
    "YOUR_ID_INSTANCE", "YOUR_API_TOKEN_INSTANCE"
)
```

### Sending a text message to a WhatsApp number

#### Link to example: [send_text_message.py](examples/async_send_text_message.py).

```python
response = await async_green_api.sending.send_message("USER_NUMBER@c.us", "Message text")

print(await response.json())
```

### All examples you can find [here](./examples)

## The full list of the library methods

| api_method                             | description                                                                                                              | documentation_link                                                                                          |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| account.get_settings                   | The method is designed to get the current settings of the account                                                        | [GetSettings](https://green-api.com/en/docs/api/account/GetSettings/)                                       |
| account.get_wa_settings                | The method is designed to get information about the WhatsApp account                                                     | [GetWaSettings](https://green-api.com/en/docs/api/account/GetWaSettings/)                                   |
| account.set_settings                   | The method is designed to set the account settings                                                                       | [SetSettings](https://green-api.com/en/docs/api/account/SetSettings/)                                       |
| account.get_state_instance             | The method is designed to get the state of the account                                                                   | [GetStateInstance](https://green-api.com/en/docs/api/account/GetStateInstance/)                             |
| account.get_status_instance            | The method is designed to get the socket connection state of the account instance with WhatsApp                          | [GetStatusInstance](https://green-api.com/en/docs/api/account/GetStatusInstance/)                           |
| account.reboot                         | The method is designed to restart the account                                                                            | [Reboot](https://green-api.com/en/docs/api/account/Reboot/)                                                 |
| account.logout                         | The method is designed to unlogin the account                                                                            | [Logout](https://green-api.com/en/docs/api/account/Logout/)                                                 |
| account.qr                             | The method is designed to get a QR code                                                                                  | [QR](https://green-api.com/en/docs/api/account/QR/)                                                         |
| account.set_profile_picture            | The method is designed to set the avatar of the account                                                                  | [SetProfilePicture](https://green-api.com/en/docs/api/account/SetProfilePicture/)                           |
| account.get_authorization_code         | The method is designed to authorize an instance by phone number                                                          | [GetAuthorizationCode](https://green-api.com/en/docs/api/account/GetAuthorizationCode/)                     |
| device.get_device_info                 | The method is designed to get information about the device (phone) on which the WhatsApp Business application is running | [GetDeviceInfo](https://green-api.com/en/docs/api/phone/GetDeviceInfo/)                                     |
| groups.create_group                    | The method is designed to create a group chat                                                                            | [CreateGroup](https://green-api.com/en/docs/api/groups/CreateGroup/)                                        |
| groups.update_group_name               | The method changes the name of the group chat                                                                            | [UpdateGroupName](https://green-api.com/en/docs/api/groups/UpdateGroupName/)                                |
| groups.get_group_data                  | The method gets group chat data                                                                                          | [GetGroupData](https://green-api.com/en/docs/api/groups/GetGroupData/)                                      |
| groups.add_group_participant           | The method adds a participant to the group chat                                                                          | [AddGroupParticipant](https://green-api.com/en/docs/api/groups/AddGroupParticipant/)                        |
| groups.remove_group_participant        | The method removes the participant from the group chat                                                                   | [RemoveGroupParticipant](https://green-api.com/en/docs/api/groups/RemoveGroupParticipant/)                  |
| groups.set_group_admin                 | The method designates a member of a group chat as an administrator                                                       | [SetGroupAdmin](https://green-api.com/en/docs/api/groups/SetGroupAdmin/)                                    |
| groups.remove_admin                    | The method deprives the participant of group chat administration rights                                                  | [RemoveAdmin](https://green-api.com/en/docs/api/groups/RemoveAdmin/)                                        |
| groups.set_group_picture               | The method sets the avatar of the group                                                                                  | [SetGroupPicture](https://green-api.com/en/docs/api/groups/SetGroupPicture/)                                |
| groups.leave_group                     | The method logs the user of the current account out of the group chat                                                    | [LeaveGroup](https://green-api.com/en/docs/api/groups/LeaveGroup/)                                          |
| journals.get_chat_history              | The method returns the chat message history                                                                              | [GetChatHistory](https://green-api.com/en/docs/api/journals/GetChatHistory/)                                |
| journals.get_message                   | The method returns a chat message                                                                                        | [GetMessage](https://green-api.com/en/docs/api/journals/GetMessage/)                                        |
| journals.last_incoming_messages        | The method returns the most recent incoming messages of the account                                                      | [LastIncomingMessages](https://green-api.com/en/docs/api/journals/LastIncomingMessages/)                    |
| journals.last_outgoing_messages        | The method returns the last sent messages of the account                                                                 | [LastOutgoingMessages](https://green-api.com/en/docs/api/journals/LastOutgoingMessages/)                    |
| queues.show_messages_queue             | The method is designed to get the list of messages that are in the queue to be sent                                      | [ShowMessagesQueue](https://green-api.com/en/docs/api/queues/ShowMessagesQueue/)                            |
| queues.clear_messages_queue            | The method is designed to clear the queue of messages to be sent                                                         | [ClearMessagesQueue](https://green-api.com/en/docs/api/queues/ClearMessagesQueue/)                          |
| marking.read_chat                      | The method is designed to mark chat messages as read                                                                     | [ReadChat](https://green-api.com/en/docs/api/marks/ReadChat/)                                               |
| receiving.receive_notification         | The method is designed to receive a single incoming notification from the notification queue                             | [ReceiveNotification](https://green-api.com/en/docs/api/receiving/technology-http-api/ReceiveNotification/) |
| receiving.delete_notification          | The method is designed to remove an incoming notification from the notification queue                                    | [DeleteNotification](https://green-api.com/en/docs/api/receiving/technology-http-api/DeleteNotification/)   |
| receiving.download_file                | The method is for downloading received and sent files                                                                    | [DownloadFile](https://green-api.com/en/docs/api/receiving/files/DownloadFile/)                             |
| sending.send_message                   | The method is designed to send a text message to a personal or group chat                                                | [SendMessage](https://green-api.com/en/docs/api/sending/SendMessage/)                                       |
| sending.send_buttons                   | The method is designed to send a message with buttons to a personal or group chat                                        | [SendButtons](https://green-api.com/en/docs/api/sending/SendButtons/)                                       |
| sending.send_template_buttons          | The method is designed to send a message with interactive buttons from the list of templates in a personal or group chat | [SendTemplateButtons](https://green-api.com/en/docs/api/sending/SendTemplateButtons/)                       |
| sending.send_list_message              | The method is designed to send a message with a selection button from a list of values to a personal or group chat       | [SendListMessage](https://green-api.com/en/docs/api/sending/SendListMessage/)                               |
| sending.send_file_by_upload            | The method is designed to send a file loaded through a form (form-data)                                                  | [SendFileByUpload](https://green-api.com/en/docs/api/sending/SendFileByUpload/)                             |
| sending.send_file_by_url               | The method is designed to send a file downloaded via a link                                                              | [SendFileByUrl](https://green-api.com/en/docs/api/sending/SendFileByUrl/)                                   |
| sending.upload_file                    | The method is designed to upload a file to the cloud storage, which can be sent using the sendFileByUrl method           | [UploadFile](https://green-api.com/en/docs/api/sending/UploadFile/)                                         |
| sending.send_location                  | The method is designed to send a geolocation message                                                                     | [SendLocation](https://green-api.com/en/docs/api/sending/SendLocation/)                                     |
| sending.send_contact                   | The method is for sending a message with a contact                                                                       | [SendContact](https://green-api.com/en/docs/api/sending/SendContact/)                                       |
| sending.send_link                      | The method is designed to send a message with a link that will add an image preview, title and description               | [SendLink](https://green-api.com/en/docs/api/sending/SendLink/)                                             |
| sending.forward_messages               | The method is designed for forwarding messages to a personal or group chat                                               | [ForwardMessages](https://green-api.com/en/docs/api/sending/ForwardMessages/)                               |
| sending.send_poll                      | The method is designed for sending messages with a poll to a private or group chat                                       | [SendPoll](https://green-api.com/en/docs/api/sending/SendPoll/)                                             |
| service_methods.check_whatsapp         | The method checks if there is a WhatsApp account on the phone number                                                     | [CheckWhatsapp](https://green-api.com/en/docs/api/service/CheckWhatsapp/)                                   |
| service_methods.get_avatar             | The method returns the avatar of the correspondent or group chat                                                         | [GetAvatar](https://green-api.com/en/docs/api/service/GetAvatar/)                                           |
| service_methods.get_contacts           | The method is designed to get a list of contacts of the current account                                                  | [GetContacts](https://green-api.com/en/docs/api/service/GetContacts/)                                       |
| service_methods.get_contact_info       | The method is designed to obtain information about the contact                                                           | [GetContactInfo](https://green-api.com/en/docs/api/service/GetContactInfo/)                                 |
| service_methods.delete_message         | The method deletes the message from chat                                                                                 | [DeleteMessage](https://green-api.com/en/docs/api/service/deleteMessage/)                                   |
| service_methods.archive_chat           | The method archives the chat                                                                                             | [ArchiveChat](https://green-api.com/en/docs/api/service/archiveChat/)                                       |
| service_methods.unarchive_chat         | The method unarchives the chat                                                                                           | [UnarchiveChat](https://green-api.com/en/docs/api/service/unarchiveChat/)                                   |
| service_methods.set_disappearing_chat  | The method is designed to change the settings of disappearing messages in chats                                          | [SetDisappearingChat](https://green-api.com/en/docs/api/service/SetDisappearingChat/)                       |
| webhooks.start_receiving_notifications | The method is designed to start receiving new notifications                                                              |                                                                                                             |
| webhooks.stop_receiving_notifications  | The method is designed to stop receiving new notifications                                                               |                                                                                                             |

## Service methods documentation

[https://green-api.com/en/docs/api/.](https://green-api.com/en/docs/api/.)

## External products

- [httpx](https://www.python-httpx.org/) - for asynchronous HTTP requests.

## License

Licensed
under [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/)
terms. Please see the [LICENSE](https://github.com/green-api/whatsapp-api-client-python/blob/master/LICENSE) file.
