from typing import List, Tuple

from src.models.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], filter_words: List[str]) -> List[Vacancy]:
    """Выборка вакансий по ключевым словам"""

    if not filter_words:
        return vacancies

    result_list = []
    search_on = False
    for vacancy in vacancies:
        vacancy_dict = vacancy.to_dict()
        for word in filter_words:

            for value in vacancy_dict.values():
                if word in str(value).lower():
                    # print(word)
                    # print(vacancy_dict)
                    result_list.append(vacancy)
                    search_on = True
                    break

            if search_on:
                search_on = False
                break

    return result_list


def filter_by_solary(vacancies: List[Vacancy], salary_range: Tuple[float, float]) -> List[Vacancy]:
    """Выборка вакансий по зарплате"""

    if not salary_range:
        return vacancies

    result_list = []
    for vacancy in vacancies:
        if salary_range[0] <= vacancy.salary <= salary_range[1]:
            result_list.append(vacancy)

    return result_list


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Выборка нескольких топовых вакансий"""

    top_vacancies = []
    for index, item in enumerate(vacancies):
        if index < top_n:
            top_vacancies.append(item)
        else:
            break

    return top_vacancies

def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка по зарплате (по убыванию)"""

    vacancies.sort(key=lambda x: x.salary, reverse=True)
    return vacancies
