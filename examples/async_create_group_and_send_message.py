import asyncio

from async_whatsapp_api_client_python import AsyncGreenAPI


async def main():
    async_green_api = AsyncGreenAPI(
        "YOUR_ID_INSTANCE", "YOUR_API_TOKEN_INSTANCE"
    )
    create_group_response = await async_green_api.groups.create_group(
        "Group Name", ["USER_NUMBER@c.us", "USER_NUMBER@c.us"]
    )
    if create_group_response.code == 200:
        print(create_group_response.data)
        send_message_response = await async_green_api.sending.send_message(
            create_group_response.data["chatId"], "Message text"
        )
        if send_message_response.code == 200:
            print(send_message_response.data)
        else:
            print(send_message_response.error)
    else:
        print(create_group_response.error)


if __name__ == '__main__':
    asyncio.run(main())
