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
            self.salary = Vacancy.__verify_data(vacancy["salary"])
            self.area = vacancy["area"]
            self.employer = vacancy["employer"]
            self.employment = vacancy["employment"]
            self.created_at = vacancy["created_at"]
            self.archived = vacancy["archived"]
            self.work_format = vacancy["work_format"]
            self.published_at = vacancy["published_at"]
            self.apply_alternate_url = vacancy["apply_alternate_url"]
            self.snippet = vacancy["snippet"]

    def __lt__(self, other):
        if not isinstance(other, (float, Vacancy)):
            raise TypeError("Операнд справа должен иметь тип float или Vacancy")

        sc = other if isinstance(other, float) else other.salary
        return self.salary < sc

    def __repr__(self):
        return f"name: {self.name_vacancy}, salary: {self.salary}, url: {self.apply_alternate_url}, snippet: {self.snippet}"

    @classmethod
    def __verify_data(cls, value: dict | float | None) -> float:
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
