from src.api.abstract_api import AbstractAPI

import requests


class HeadHunterAPI(AbstractAPI):
    """Класс для получения вакансий через API"""

    def _connect_to_api(self, param: str) -> dict | None:

        url = "https://api.hh.ru/vacancies"

        param = param
        head = "HH-User-Agent: "

        response = requests.get(url, param)

        if response.status_code == 200:
            return response.json()
        else:
            return None


    def get_vacancies(self, search_query: str) -> list[dict] | None:
        """Получение вакансий через API Head Hunter"""

        response = self._connect_to_api(search_query)
        print(response)
        if response is None:
            return None

        else:
            vacancies = []
            for item in response["items"]:
                vacancy = dict()
                vacancy["id"] = item["id"]

                vacancies.append(vacancy)

            return vacancies
