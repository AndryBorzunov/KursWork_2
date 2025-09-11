import json
from pprint import pprint

import requests

from src.api.abstract_api import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """Класс для получения вакансий через API"""

    def _connect_to_api(self, query_parameters: str) -> dict | None:

        url = "https://api.hh.ru/vacancies"

        params = json.loads(query_parameters)
        headers = {"HH-User-Agent": "Kurswork2/1.0 (andry73@yandex.ru)"}

        response = requests.get(url, params, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_vacancies(self, search_query: str) -> list[dict] | None:
        """Получение вакансий через API Head Hunter"""

        response = self._connect_to_api(search_query)
        # pprint(response)
        if response is None:
            return None

        else:
            vacancies = []
            for item in response["items"]:
                vacancy = dict()
                vacancy["id"] = item["id"]
                vacancy["name"] = item["name"]
                if "professional_roles" in item:
                    vacancy["professional_roles"] = item["professional_roles"]
                if "salary" in item:
                    vacancy["salary"] = item["salary"]
                if "area" in item:
                    vacancy["area"] = item["area"]
                if "employer" in item:
                    vacancy["employer"] = item["employer"]
                if "employment" in item:
                    vacancy["employment"] = item["employment"]
                if "created_at" in item:
                    vacancy["created_at"] = item["created_at"]
                if "archived" in item:
                    vacancy["archived"] = item["archived"]
                if "work_format" in item:
                    vacancy["work_format"] = item["work_format"]
                if "published_at" in item:
                    vacancy["published_at"] = item["published_at"]
                if "apply_alternate_url" in item:
                    vacancy["apply_alternate_url"] = item["apply_alternate_url"]
                if "snippet" in item:
                    vacancy["snippet"] = item["snippet"]

                vacancies.append(vacancy)

            found_dict = {"found": response["found"], "page": response["page"], "per_page": response["per_page"]}
            vacancies.append(found_dict)

            return vacancies
