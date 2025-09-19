import pytest

from src.utils.filters import filter_vacancies, filter_by_solary
from src.models.vacancy import Vacancy


@pytest.fixture
def data_in():
    return [
    {
        "id": "125270081",
        "name": "Разработчик (Python Django)",
        "salary": 300000.0,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125270081",
        "snippet": {
            "Навыки": "Опыт от 6-ти лет разработки на следующем стеке: <highlighttext>Python</highlighttext>\\Django, PostgreSQL, REST API, GraphQL, Redis, ClickHouse, RabbitMQ, Kafka, Swagger...",
            "Обязанности": "Участие в создании cloud native решений. Развитие бэкенда (<highlighttext>Python</highlighttext>\\Django) функционально насыщенной логистической платформы с веб-клиентом на Angular и..."
        }
    },
    {
        "id": "125401126",
        "name": "Senior Backend разработчик (Python)",
        "salary": 250000.0,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125401126",
        "snippet": {
            "Навыки": "Опыт backend-разработки коммерческих продуктов от 3 лет. Свободное владение <highlighttext>Python</highlighttext> 3 и Django REST framework. Уверенное знание SQL (предпочтительно...",
            "Обязанности": "Разработкой новых и развитием существующих функций в рамках платформы. Покрытием тестами текущей кодовой базы. Проектированием архитектуры и разработкой серверной части..."
        }
    },
    {
        "id": "125483778",
        "name": "Junior DevOps / Python backend engineer",
        "salary": 150000.0,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125483778",
        "snippet": {
            "Навыки": "Интерес к DevOps и желание развиваться именно в этой сфере. Знание <highlighttext>Python</highlighttext> на уровне написания простых сервисов, скриптов. ",
            "Обязанности": "Следить за мониторингом и логированием. Автоматизировать рутинные задачи с помощью скриптов (<highlighttext>Python</highlighttext>, Bash). Участвовать в разработке бэкенда (Django + FastAPI..."
        }
    }
]

@pytest.mark.parametrize(
    "words, filtered",
    [
        (
            ["django", "sql"],
            [
                {
                    "id": "125270081",
                    "name": "Разработчик (Python Django)",
                    "salary": 300000.0,
                    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125270081",
                    "snippet": {
                        "Навыки": "Опыт от 6-ти лет разработки на следующем стеке: <highlighttext>Python</highlighttext>\\Django, PostgreSQL, REST API, GraphQL, Redis, ClickHouse, RabbitMQ, Kafka, Swagger...",
                        "Обязанности": "Участие в создании cloud native решений. Развитие бэкенда (<highlighttext>Python</highlighttext>\\Django) функционально насыщенной логистической платформы с веб-клиентом на Angular и..."
                    }
                },
            ]
        ),
        (
            ["django", "backend"],
            [
                {
                    "id": "125270081",
                    "name": "Разработчик (Python Django)",
                    "salary": 300000.0,
                    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125270081",
                    "snippet": {
                        "Навыки": "Опыт от 6-ти лет разработки на следующем стеке: <highlighttext>Python</highlighttext>\\Django, PostgreSQL, REST API, GraphQL, Redis, ClickHouse, RabbitMQ, Kafka, Swagger...",
                        "Обязанности": "Участие в создании cloud native решений. Развитие бэкенда (<highlighttext>Python</highlighttext>\\Django) функционально насыщенной логистической платформы с веб-клиентом на Angular и..."
                    }
                },
                {
                    "id": "125401126",
                    "name": "Senior Backend разработчик (Python)",
                    "salary": 250000.0,
                    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125401126",
                    "snippet": {
                        "Навыки": "Опыт backend-разработки коммерческих продуктов от 3 лет. Свободное владение <highlighttext>Python</highlighttext> 3 и Django REST framework. Уверенное знание SQL (предпочтительно...",
                        "Обязанности": "Разработкой новых и развитием существующих функций в рамках платформы. Покрытием тестами текущей кодовой базы. Проектированием архитектуры и разработкой серверной части..."
                    }
                },
                {
                    "id": "125483778",
                    "name": "Junior DevOps / Python backend engineer",
                    "salary": 150000.0,
                    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125483778",
                    "snippet": {
                        "Навыки": "Интерес к DevOps и желание развиваться именно в этой сфере. Знание <highlighttext>Python</highlighttext> на уровне написания простых сервисов, скриптов. ",
                        "Обязанности": "Следить за мониторингом и логированием. Автоматизировать рутинные задачи с помощью скриптов (<highlighttext>Python</highlighttext>, Bash). Участвовать в разработке бэкенда (Django + FastAPI..."
                    }
                }
            ]
        )
    ],
)
def test_filter_vacancies(data_in, words, filtered):
    vacancies = Vacancy.cast_to_object_list(data_in)
    assert str(filter_vacancies(vacancies, words)) == str(Vacancy.cast_to_object_list(filtered))


@pytest.mark.parametrize(
    "salary_range, filtered",
    [
        (
            (260000, 400000),
            [
                {
                    "id": "125270081",
                    "name": "Разработчик (Python Django)",
                    "salary": 300000.0,
                    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125270081",
                    "snippet": {
                        "Навыки": "Опыт от 6-ти лет разработки на следующем стеке: <highlighttext>Python</highlighttext>\\Django, PostgreSQL, REST API, GraphQL, Redis, ClickHouse, RabbitMQ, Kafka, Swagger...",
                        "Обязанности": "Участие в создании cloud native решений. Развитие бэкенда (<highlighttext>Python</highlighttext>\\Django) функционально насыщенной логистической платформы с веб-клиентом на Angular и..."
                    }
                },
            ]
        ),
    ]
)
def test_filter_by_solary(data_in, salary_range, filtered):
    vacancies = Vacancy.cast_to_object_list(data_in)
    assert str(filter_by_solary(vacancies, salary_range)) == str(Vacancy.cast_to_object_list(filtered))
