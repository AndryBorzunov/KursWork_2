import json
from typing import Any, Dict, List, Tuple

from src.models.vacancy import Vacancy
from src.storage.abstract_storage import AbstractStorage
from src.utils.filters import filter_by_solary, filter_vacancies


class JsonStorage(AbstractStorage):
    """Класс для хранения данных в json-файле"""

    __filename: str
    __vacancies_saved: List[Dict[str, Any]]

    def __init__(self, filename: str = "data/vacancies.json"):
        self.__filename = filename
        self.__vacancies_saved = []

    def __read_vacancy(self) -> List[Dict[str, Any]]:
        """Чтение вакансий из файла"""
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                # Читаем данные из файла
                self.__vacancies_saved = json.load(file)
                # print(self.__vacancies_saved)
        except FileNotFoundError:
            print("Создаём новый файл")

        return self.__vacancies_saved

    def __write_vacancies(self, vacancies: List[Dict[str, Any]]) -> None:
        """Запись списка вакансий в файл"""

        try:
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(vacancies, file, ensure_ascii=False, indent=4)
        except BaseException as err:
            print(f"Error:{err}")

    @classmethod
    def __check_duplicated(cls, vacancies: List[Dict[str, Any]], new_vacancy: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Проверка дубликатов"""

        result_search = False
        for index, item in enumerate(vacancies):
            # Сравниваем id номер вакансии
            if item["id"] == new_vacancy["id"]:
                # обновляем данные о вакансии
                vacancies[index] = new_vacancy
                result_search = True

        if not result_search:
            vacancies.append(new_vacancy)

        return vacancies

    def add_vacancy(self, vacancy: Dict[str, Any]) -> None:
        """Добавление вакансии"""

        vacancy_saved = self.__read_vacancy()
        if len(vacancy_saved) == 0:
            vacancy_saved.append(vacancy)

        else:
            vacancy_saved = self.__check_duplicated(vacancy_saved, vacancy)

        self.__write_vacancies(vacancy_saved)

    def delete_vacancy(self, vacancy_id: str) -> None:
        """Удаление вакансии по id"""

        vacancy_saved = self.__read_vacancy()
        for item in vacancy_saved:
            if item["id"] == vacancy_id:
                vacancy_saved.remove(item)
                break

        self.__write_vacancies(vacancy_saved)

    def filter_vacancies(self, filter_words: List[str]) -> List[Dict[str, Any]]:
        """Фильтрация вакансий по ключевым словам"""
        vacancy_saved = self.__read_vacancy()
        vacancy_objects = Vacancy.cast_to_object_list(vacancy_saved)
        filtered = filter_vacancies(vacancy_objects, filter_words)

        filtered_dicts = []
        for item in filtered:
            filtered_dicts.append(item.to_dict())

        return filtered_dicts

    def filter_vacancies_by_salary(self, salary_range: Tuple[float, float]) -> List[Dict[str, Any]]:
        """Фильтрация вакансий по зарплате"""
        vacancy_saved = self.__read_vacancy()
        vacancy_objects = Vacancy.cast_to_object_list(vacancy_saved)
        filtered = filter_by_solary(vacancy_objects, salary_range)

        filtered_dicts = []
        for item in filtered:
            filtered_dicts.append(item.to_dict())

        return filtered_dicts
