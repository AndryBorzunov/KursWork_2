from typing import Any


class Vacancy:

    __slots__ = (
        "id_vacancy",
        "name_vacancy",
        "professional_roles",
        "salary",
        "area",
        "employer",
        "employment",
        "created_at",
        "archived",
        "work_format",
        "published_at",
        "apply_alternate_url",
        "snippet",
    )

    def __init__(self, vacancy: dict) -> None:

        if "id" in vacancy:
            self.id_vacancy = vacancy["id"]
            self.name_vacancy = vacancy["name"]
            self.professional_roles = vacancy["professional_roles"]
            self.salary = Vacancy.__verify_salary(vacancy["salary"])
            self.area = vacancy["area"]
            self.employer = vacancy["employer"]
            self.employment = vacancy["employment"]
            self.created_at = vacancy["created_at"]
            self.archived = vacancy["archived"]
            self.work_format = vacancy["work_format"]
            self.published_at = vacancy["published_at"]
            self.apply_alternate_url = vacancy["apply_alternate_url"]
            self.snippet = vacancy["snippet"]

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, (float, Vacancy)):
            raise TypeError("Операнд справа должен иметь тип float или Vacancy")

        sc = other if isinstance(other, float) else other.salary
        return self.salary < sc

    def __repr__(self) -> str:
        return f"name: {self.name_vacancy}, salary: {self.salary}, url: {self.apply_alternate_url}, snippet: {self.snippet}"

    def __str__(self) -> str:
        return "{" + f"name: {self.name_vacancy}, salary: {self.salary}, url: {self.apply_alternate_url}" + "}"

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
        vacancy_dict["id"] = self.id_vacancy
        vacancy_dict["name"] = self.name_vacancy
        vacancy_dict["salary"] = self.salary
        vacancy_dict["url"] = self.apply_alternate_url
        vacancy_dict["snippet"] = self.snippet

        return vacancy_dict
