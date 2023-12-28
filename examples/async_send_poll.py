import asyncio

from async_whatsapp_api_client_python import AsyncGreenAPI


async def main():
    async_green_api = AsyncGreenAPI(
        "YOUR_ID_INSTANCE", "YOUR_API_TOKEN_INSTANCE"
    )
    response = await async_green_api.sending.send_poll(
        "USER_NUMBER@c.us",
        "Please choose a color:",
        [
            {"optionName": "Red"},
            {"optionName": "Green"},
            {"optionName": "Blue"}
        ]
    )

    print(response.data)


if __name__ == '__main__':
    asyncio.run(main())
