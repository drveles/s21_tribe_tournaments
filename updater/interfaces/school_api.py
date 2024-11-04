"""
Connecting to school 21 API
"""

import os
import requests


class AuthInSchoolAPI:
    def __init__(self) -> None:
        self.__auth_login = os.getenv("EDU_SCHOOL_LOGIN")
        self.__auth_password = os.getenv("EDU_SCHOOL_PASSWORD")
        if not self.__auth_login or not self.__auth_password:
            raise EnvironmentError(
                "Can't get EDU_SCHOOL_LOGIN or EDU_SCHOOL_PASSWORD from environment"
            )
        self.__auth_url = "https://auth.sberclass.ru/auth/realms/EduPowerKeycloak/protocol/openid-connect/token"

    def get_auth_tocken_to_api(self) -> str:
        """
        Auth and return token: `Bearer $token`
        """
        response = requests.post(
            url=self.__auth_url,
            data={
                "username": self.__auth_login,
                "password": self.__auth_password,
                "grant_type": "password",
                "client_id": "s21-open-api",
            },
            timeout=5,
        )
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(
                f"Can't access get Auth API. Status code: {response.status_code}, text: {response.text}"
            )

        access_token = response.json().get("access_token", "")
        if not access_token:
            raise ValueError("Failed get token from Auth API")

        return "Bearer " + access_token


class SchoolAPI:
    def __init__(self) -> None:
        self.__stock_api_endpoint = (
            "https://edu-api.21-school.ru/services/21-school/api/v1",
        )
        self.__campuses_with_uuid = {
            "Kazan": "7c293c9c-f28c-4b10-be29-560e4b000a34",
        }

        self.__coalitions_with_id = {
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

        def get_coalitions_participants(self) -> set:
            # /coalitions/{coalitionId}/participants
            pass
