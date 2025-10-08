import pytest

from src.models.vacancy import Vacancy


@pytest.fixture
def vacancy_in():
    return {
        "id": "123695397",
        "name": "Senior Python Developer",
        "salary": 350000.0,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=123695397",
        "snippet": {
            "requirement": "Отличное знание Python и опыт backend-разработки. - Понимание принципов асинхронного программирования. - Опыт работы с FastAPI. - Опыт работы с PostgreSQL. - ",
            "responsibility": "Перевод существующего монолита на микросервисную архитектуру. - Разработка и сопровождение backend-решений: рефакторинг, оптимизация, исправление ошибок, покрытие тестами, ведение технической документации. - ",
        },
    }


@pytest.fixture
def vacancy_out():
    return {
        "id": "123695397",
        "name": "Senior Python Developer",
        "salary": 350000.0,
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=123695397",
        "snippet": {
            "Навыки": "Отличное знание Python и опыт backend-разработки. - Понимание принципов асинхронного программирования. - Опыт работы с FastAPI. - Опыт работы с PostgreSQL. - ",
            "Обязанности": "Перевод существующего монолита на микросервисную архитектуру. - Разработка и сопровождение backend-решений: рефакторинг, оптимизация, исправление ошибок, покрытие тестами, ведение технической документации. - ",
        },
    }


@pytest.mark.parametrize(
    "data_input, id_vacancy, name, salary, url",
    [
        (
            {
                "id": "123695397",
                "name": "Senior Python Developer",
                "salary": 350000.0,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=123695397",
                "snippet": {
                    "requirement": "Отличное знание Python и опыт backend-разработки. - Понимание принципов асинхронного программирования. - Опыт работы с FastAPI. - Опыт работы с PostgreSQL. - ",
                    "responsibility": "Перевод существующего монолита на микросервисную архитектуру. - Разработка и сопровождение backend-решений: рефакторинг, оптимизация, исправление ошибок, покрытие тестами, ведение технической документации. - ",
                },
            },
            "123695397",
            "Senior Python Developer",
            350000,
            "https://hh.ru/applicant/vacancy_response?vacancyId=123695397",
        )
    ],
)
def test_init(data_input, id_vacancy, name, salary, url):
    vacancy = Vacancy(data_input)
    assert vacancy.id_vacancy == id_vacancy
    assert vacancy.name_vacancy == name
    assert vacancy.salary == salary
    assert vacancy.url_vacancy == url


def test_to_dict(vacancy_in, vacancy_out):
    vacancy = Vacancy(vacancy_in)
    assert vacancy.to_dict() == vacancy_out
