from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API платформ с вакансиями"""

    @abstractmethod
    def _connect_to_api(self, query_parameters: str) -> dict | None:
        """Подключение к API"""
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str) -> list[dict] | None:
        """Получение вакансий по поисковому запросу"""
        pass
