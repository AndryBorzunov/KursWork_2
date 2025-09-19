import pytest
from unittest.mock import patch

from src.storage.json_storage import JsonStorage


@pytest.fixture
def vacancy():
    return {
        "id": "123695397",
        "name": "Senior Python Developer",
        "salary": 350000,
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=123695397",
        "snippet": {
            "requirement": "Отличное знание Python и опыт backend-разработки. - Понимание принципов асинхронного программирования. - Опыт работы с FastAPI. - Опыт работы с PostgreSQL. - ",
            "responsibility": "Перевод существующего монолита на микросервисную архитектуру. - Разработка и сопровождение backend-решений: рефакторинг, оптимизация, исправление ошибок, покрытие тестами, ведение технической документации. - "
        }
    }

@pytest.fixture
def data_output():
    return [
    {
        "id": "123695397",
        "name": "Senior Python Developer",
        "salary": 350000,
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=123695397",
        "snippet": {
            "requirement": "Отличное знание Python и опыт backend-разработки. - Понимание принципов асинхронного программирования. - Опыт работы с FastAPI. - Опыт работы с PostgreSQL. - ",
            "responsibility": "Перевод существующего монолита на микросервисную архитектуру. - Разработка и сопровождение backend-решений: рефакторинг, оптимизация, исправление ошибок, покрытие тестами, ведение технической документации. - "
        }
    },
    {
        "id": "125122349",
        "name": "Tech Lead / Ведущий разработчик (Python, Fintech/Blockchain)",
        "salary": 350000,
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=125122349",
        "snippet": {
            "requirement": "Опыт в разработке: не менее 7 лет в коммерческой разработке и опыт на позиции лида или старшего инженера. ",
            "responsibility": "Архитектура: спроектировать и реализовать надежную, масштабируемую бэкенд-архитектуру для финтех-платформы, поддерживающую двухконтурную модель (публичное демо на EVM-блокчейне и..."
        }
    },
    {
        "id": "125123572",
        "name": "Инженер по численному моделированию (пористые среды, FVM/FIM, Python)",
        "salary": 450000,
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=125123572",
        "snippet": {
            "requirement": "Опыт математического моделирования с использованием численных методов. Опыт решения задач механики жидкости / газа / плазмы. Опыт разработки на Python с использованием...",
            "responsibility": "Улучшение реализации симулятора трёхфазной фильтрации (вода/нефть/эмульсия) в многослойном пласте с учётом частичной взаимной растворимости фаз, неньютоновской реологии, адсорбции..."
        }
    }
]


@pytest.fixture
def data_add():
    return [
    {
        "id": "123695397",
        "name": "Senior Python Developer",
        "salary": 350000,
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=123695397",
        "snippet": {
            "requirement": "Отличное знание Python и опыт backend-разработки. - Понимание принципов асинхронного программирования. - Опыт работы с FastAPI. - Опыт работы с PostgreSQL. - ",
            "responsibility": "Перевод существующего монолита на микросервисную архитектуру. - Разработка и сопровождение backend-решений: рефакторинг, оптимизация, исправление ошибок, покрытие тестами, ведение технической документации. - "
        }
    },
    {
        "id": "125122349",
        "name": "Tech Lead / Ведущий разработчик (Python, Fintech/Blockchain)",
        "salary": 350000,
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=125122349",
        "snippet": {
            "requirement": "Опыт в разработке: не менее 7 лет в коммерческой разработке и опыт на позиции лида или старшего инженера. ",
            "responsibility": "Архитектура: спроектировать и реализовать надежную, масштабируемую бэкенд-архитектуру для финтех-платформы, поддерживающую двухконтурную модель (публичное демо на EVM-блокчейне и..."
        }
    },
    {
        "id": "125123572",
        "name": "Инженер по численному моделированию (пористые среды, FVM/FIM, Python)",
        "salary": 450000,
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=125123572",
        "snippet": {
            "requirement": "Опыт математического моделирования с использованием численных методов. Опыт решения задач механики жидкости / газа / плазмы. Опыт разработки на Python с использованием...",
            "responsibility": "Улучшение реализации симулятора трёхфазной фильтрации (вода/нефть/эмульсия) в многослойном пласте с учётом частичной взаимной растворимости фаз, неньютоновской реологии, адсорбции..."
        }
    },
    {
        "id": "123695397",
        "name": "Senior Python Developer",
        "salary": 350000,
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=123695397",
        "snippet": {
            "requirement": "Отличное знание Python и опыт backend-разработки. - Понимание принципов асинхронного программирования. - Опыт работы с FastAPI. - Опыт работы с PostgreSQL. - ",
            "responsibility": "Перевод существующего монолита на микросервисную архитектуру. - Разработка и сопровождение backend-решений: рефакторинг, оптимизация, исправление ошибок, покрытие тестами, ведение технической документации. - "
        }
    }
]


@patch("src.storage.json_storage.JsonStorage._read_vacancy")
def test_read_vacancy(mock_read_file, vacancy, data_output, data_add):
    mock_file = mock_read_file.return_value
    mock_file.return_value = data_output
    js = JsonStorage("data/vacancies.json")
    assert js.add_vacancy(vacancy) is None
    mock_read_file.assert_called_once_with()

