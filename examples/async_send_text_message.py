import asyncio

from async_whatsapp_api_client_python import AsyncGreenAPI


async def main():
    async_green_api = AsyncGreenAPI(
        "YOUR_ID_INSTANCE", "YOUR_API_TOKEN_INSTANCE"
    )

    response = await async_green_api.sending.send_message("USER_NUMBER@c.us", "Message text")

    print(response.data)


if __name__ == '__main__':
    asyncio.run(main())
