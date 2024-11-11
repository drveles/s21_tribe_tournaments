"""
Connecting to School 21 API
"""

import asyncio
import aiohttp
import logging
from asgiref.sync import async_to_sync
from .auth_school_api import AuthInSchoolAPI


class SchoolAPI:
    def __init__(self) -> None:
        self.__stock_api_endpoint = (
            "https://edu-api.21-school.ru/services/21-school/api/v1"
        )
        self.__campuses_with_uuid = {
            "Kazan": "7c293c9c-f28c-4b10-be29-560e4b000a34",
        }
        self.__campus_tribes_with_id = {
            "Kazan": {
                "Aer": 124,
                "Anglerfish": 92,
                "Aqua": 123,
                "Ignis": 125,
                "Moray eels": 91,
                "Scorpionfish": 89,
                "Terra": 126,
                "Trionics": 90,
            }
        }  # GET /campuses/{campusId}/coalitions
        self.__token = AuthInSchoolAPI.get_auth_tocken_to_api()

    async def __fetch_tribe_members_async(self, tribe_id: str) -> dict:
        full_url = f"{self.__stock_api_endpoint}/coalitions/{tribe_id}/participants?limit=500&offset=0"
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=full_url,
                headers={"Authorization": self.__token},
                ssl=False,
            ) as response:
                if response.status == 429:
                    logging.error(f"429 status code, retrying {full_url}")
                    await asyncio.sleep(0.1)
                    return await self.__fetch_tribe_members_async(tribe_id)
                elif response.status > 200:
                    raise aiohttp.ServerConnectionError(
                        f"Code {response.status} for request: GET {full_url}"
                    )

                result = await response.json()
                return result.get("participants", [])

    async def _get_campus_tribes_memebers_async(self, name: str) -> dict:
        if (
            name not in self.__campuses_with_uuid
            or name not in self.__campus_tribes_with_id
        ):
            raise KeyError(f"Campus {name} not presented in SchoolAPI")

        tasks = list()
        for tribe_id in self.__campus_tribes_with_id[name].values():
            tasks.append(
                asyncio.create_task(self.__fetch_tribe_members_async(tribe_id))
            )

        results_arr = await asyncio.gather(*tasks)

        tribe_data = dict(zip(self.__campus_tribes_with_id[name].keys(), results_arr))
        return tribe_data

    def get_campus_tribes_memebers(self, name: str) -> dict:
        return async_to_sync(self._get_campus_tribes_memebers_async)(name)


if __name__ == "__main__":
    schoolAPI = SchoolAPI()
    schoolAPI.get_campus_tribes_memebers("Kazan")
