import asyncio
from datetime import datetime
from json import dumps

from async_whatsapp_api_client_python import AsyncGreenAPI


async def main():
    async_green_api = AsyncGreenAPI(
        "YOUR_ID_INSTANCE", "YOUR_API_TOKEN_INSTANCE"
    )

    await async_green_api.webhooks.start_receiving_notifications(handler)


def handler(type_webhook: str, body: dict) -> None:
    handlers = {
        "incomingMessageReceived": incoming_message_received,
        "outgoingMessageReceived": outgoing_message_received,
        "outgoingAPIMessageReceived": outgoing_api_message_received,
        "outgoingMessageStatus": outgoing_message_status,
        "stateInstanceChanged": state_instance_changed,
        "deviceInfo": device_info,
        "incomingCall": incoming_call,
        "statusInstanceChanged": status_instance_changed,
    }
    if type_webhook in handlers:
        handlers[type_webhook](body)


def get_notification_time(timestamp: int) -> str:
    return str(datetime.fromtimestamp(timestamp))


def print_notification(notification_type: str, time: str, data: dict) -> None:
    formatted_data = dumps(data, ensure_ascii=False, indent=4)
    print(f"New {notification_type} at {time} with data: {formatted_data}", end="\n\n")


def incoming_message_received(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    print_notification("incoming message", time, body)


def outgoing_message_received(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    print_notification("outgoing message", time, body)


def outgoing_api_message_received(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    print_notification("outgoing API message", time, body)


def outgoing_message_status(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    response = f"Status of sent message has been updated at {time} with data: {dumps(body, ensure_ascii=False, indent=4)}"
    print(response, end="\n\n")


def state_instance_changed(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    print_notification("current instance state", time, body)


def device_info(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    response = f"Current device information at {time} with data: {dumps(body, ensure_ascii=False, indent=4)}"
    print(response, end="\n\n")


def incoming_call(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    print_notification("incoming call", time, body)


def status_instance_changed(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    print_notification("current instance status", time, body)


if __name__ == '__main__':
    asyncio.run(main())
