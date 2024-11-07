"""
Connecting to School 21 API
"""

import asyncio
import aiohttp
from asgiref.sync import async_to_sync

from auth_school_api import AuthInSchoolAPI


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
                return await response.json()

    async def get_campus_tribes_memebers_async(self, name: str) -> dict:
        if (
            name not in self.__campuses_with_uuid
            or name not in self.__campus_tribes_with_id
        ):
            raise KeyError(f"Campus {name} not presented in SchoolAPI")

        tribe_results = dict()

        for tribe_name, tribe_id in self.__campus_tribes_with_id[name].items():
            task = asyncio.create_task(self.__fetch_tribe_members_async(tribe_id))
            tribe_results[tribe_name] = task
        results = await asyncio.gather(*tribe_results.values())

        tribe_data = {
            tribe_name: result
            for tribe_name, result in zip(tribe_results.keys(), results)
        }
        return tribe_data

    def get_campus_tribes_memebers(self, name: str, is_async: bool = True) -> dict:
        if is_async:
            return async_to_sync(self.get_campus_tribes_memebers_async)(name)
        else: 
            # return async_to_sync(self.get_campus_tribes_memebers_async)(name)
            pass
 

if __name__ == "__main__":
    schoolAPI = SchoolAPI()

    schoolAPI.get_campus_tribes_memebers("Kazan", is_async=True)

