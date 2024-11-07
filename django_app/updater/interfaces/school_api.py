"""
Connecting to School 21 API
"""

from auth_school_api import AuthInSchoolAPI


class SchoolAPI:
    def __init__(self) -> None:
        self.__stock_api_endpoint = (
            "https://edu-api.21-school.ru/services/21-school/api/v1",
        )
        self.__campuses_with_uuid = {
            "Kazan": "7c293c9c-f28c-4b10-be29-560e4b000a34",
        }
        self.__campus_coalitions_with_id = {
            "Kazan": {
                "Aer": 124,
                "Anglerfish": 92,
                "Aqua": 123,
                "Ignis": 125,
                "Moray eels": 91,
                "Scorpionfish": 89,
                "Terra": 182,
                "Trionics": 90,
            }
        }  # GET /campuses/{campusId}/coalitions

    async def __acync_fetch_coalition_participants(self, full_url: str) -> set:
        pass

    def _get_coalitions_participants(self, campus_name: str) -> dict:
        # need cache

        coalitions_participants = dict()

        for coalitions in self.__campus_coalitions_with_id[campus_name]:
            for coalition_name, coalition_id in coalitions.items():
                print(coalition_name, coalition_id)

    async def __acync_fetch_participant_rank(self, full_url: str) -> dict:
        pass

    def _get_particapant_rank(self, login: str) -> int:

        pass

    def get_all_campus_participant_info(self, campus_name: str) -> dict:
        if campus_name not in self.__campus_coalitions_with_id:
            raise KeyError(f"Invalid name of campus: {campus_name}")


if __name__ == "__main__":
    schoolAPI = SchoolAPI()

    schoolAPI.get_coalitions_participants()
