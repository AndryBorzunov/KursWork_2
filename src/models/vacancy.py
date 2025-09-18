from typing import Any


class Vacancy:

    __slots__ = (
        "__id_vacancy",
        "__name_vacancy",
        "__professional_roles",
        "__salary",
        "__area",
        "__employer",
        "__employment",
        "__created_at",
        "__archived",
        "__work_format",
        "__published_at",
        "__apply_alternate_url",
        "__snippet",
    )

    def __init__(self, vacancy: dict) -> None:

        if "id" in vacancy:
            self.__id_vacancy = vacancy["id"]
        if "name" in vacancy:
            self.__name_vacancy = vacancy["name"]
        if "professional_roles" in vacancy:
            self.__professional_roles = vacancy["professional_roles"]
        if "salary" in vacancy:
            self.__salary = Vacancy.__verify_salary(vacancy["salary"])
        if "area" in vacancy:
            self.__area = vacancy["area"]
        if "employer" in vacancy:
            self.__employer = vacancy["employer"]
        if "employment" in vacancy:
            self.__employment = vacancy["employment"]
        if "created_at" in vacancy:
            self.__created_at = vacancy["created_at"]
        if "archived" in vacancy:
            self.__archived = vacancy["archived"]
        if "work_format" in vacancy:
            self.__work_format = vacancy["work_format"]
        if "published_at" in vacancy:
            self.__published_at = vacancy["published_at"]
        if "apply_alternate_url" in vacancy:
            self.__apply_alternate_url = vacancy["apply_alternate_url"]
        if "snippet" in vacancy:
            self.__snippet = Vacancy.__verify_snippet(vacancy["snippet"])

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, (float, Vacancy)):
            raise TypeError("Операнд справа должен иметь тип float или Vacancy")

        sc = other if isinstance(other, float) else other.__salary
        return self.__salary < sc

    def __repr__(self) -> str:
        return f"Вакансия: {self.__name_vacancy}, зарплата: {self.__salary}, url: {self.__apply_alternate_url}, snippet: {self.__snippet}"

    def __str__(self) -> str:
        return "{" + f"name: {self.__name_vacancy}, зарплата: {self.__salary}, url: {self.__apply_alternate_url}" + "}"

    @classmethod
    def __verify_salary(cls, value: dict | float | None) -> float | Any:
        """Верификация данных по зарплате"""

        if value is None:
            return 0

        if not isinstance(value, (float, dict)):
            raise TypeError("Тип данных должен быть или словарь или float")

        elif isinstance(value, dict):
            if "from" in value and not value["from"] is None:
                return value["from"]
            elif "to" in value and not value["to"] is None:
                return value["to"]
            else:
                return 0
        else:
            return value

    @classmethod
    def __verify_snippet(cls, value: dict[str, Any] | str | None) -> dict[str, Any] | str:
        """Верификация данных по требованиям к кандидату"""

        if isinstance(value, dict):
            result = dict()
            if "requirement" in value:
                result["Навыки"] = value["requirement"]
            if "responsibility" in value:
                result["Обязанности"] = value["responsibility"]

            return result

        else:
            return value


    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list[Any]:
        """Преобразование списка словарей вакансий в список экземпляров класса Vacancy"""

        vacancies_obj = []
        for item in vacancies:
            # Создаём объект и добавляем его в список
            if "id" in item:
                vacancy = Vacancy(item)
                vacancies_obj.append(vacancy)

        return vacancies_obj

    def to_dict(self) -> dict:

        vacancy_dict = dict()
        vacancy_dict["id"] = self.__id_vacancy
        vacancy_dict["name"] = self.__name_vacancy
        vacancy_dict["salary"] = self.__salary
        vacancy_dict["url"] = self.__apply_alternate_url
        vacancy_dict["snippet"] = self.__snippet

        return vacancy_dict

    @property
    def salary(self) -> float:
        return self.__salary

    @property
    def id_vacancy(self) -> str:
        return self.__id_vacancy

    @property
    def name_vacancy(self) -> str:
        return self.__name_vacancy

    @property
    def work_format(self) -> str:
        return self.__work_format

    @property
    def url_vacancy(self) -> str:
        return  self.__apply_alternate_url

    @property
    def snippet(self) -> str | dict[str, Any]:
        return self.__snippet
