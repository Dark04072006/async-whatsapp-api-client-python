import asyncio
from os.path import basename
from urllib.parse import urlparse

from async_whatsapp_api_client_python import AsyncGreenAPI


async def main():
    async_green_api = AsyncGreenAPI(
        "YOUR_ID_INSTANCE", "YOUR_API_TOKEN_INSTANCE"
    )
    upload_file_response = await async_green_api.sending.upload_file(
        "data/rates.png"
    )
    if upload_file_response.code == 200:
        print(upload_file_response.data)

        url_file = upload_file_response.data["urlFile"]

        url = urlparse(url_file)
        file_name = basename(url.path)

        send_file_by_url_response = await async_green_api.sending.send_file_by_url(
            "USER_NUMBER@c.us", url_file, file_name
        )
        if send_file_by_url_response.code == 200:
            print(send_file_by_url_response.data)
        else:
            print(send_file_by_url_response.error)
    else:
        print(upload_file_response.error)


if __name__ == '__main__':
    asyncio.run(main())
