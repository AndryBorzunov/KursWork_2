from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple


class AbstractStorage(ABC):
    """Абстрактный класс для работы с сохраненными вакансиями"""

    @abstractmethod
    def add_vacancy(self, vacancy: Dict[str, Any]) -> None:
        """Добавляет вакансию в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: str) -> None:
        """Удаляет вакансию из файла по id"""
        pass

    @abstractmethod
    def filter_vacancies(self, filter_words: List[str]) -> List[Dict[str, Any]]:
        """Фильтрует вакансии по ключевым словам"""
        pass

    @abstractmethod
    def filter_vacancies_by_salary(self, salary_range: Tuple[float, float]) -> List[Dict[str, Any]]:
        """Фильтрует вакансии по диапазону зарплат"""
        pass
