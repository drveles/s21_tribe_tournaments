"""
Getting Bearer token to School 21 API
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
