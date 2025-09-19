from unittest.mock import patch

import pytest

from src.api.hh_api import HeadHunterAPI


@pytest.mark.parametrize(
    "data_input, result",
    [
        (
            {"text": "python", "page": "0", "per_page": "1"},
            {
                "items": [
                    {
                        "id": "125426940",
                        "name": "Backend-разработчик Python/Django",
                        "salary": 250000,
                        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125426940",
                    }
                ]
            },
        ),
    ],
)
@patch("requests.get")
def test_get_amount_rub(mock_get, data_input, result):
    mock_get.return_value.json.return_value = result
    # mock_get.return_value.status_code.return_value = 200
    hh_api = HeadHunterAPI()
    assert hh_api._connect_to_api(data_input) == result
    mock_get.assert_called_once_with(
        "https://api.hh.ru/vacancies",
        {"text": "python", "page": "0", "per_page": "1"},
        headers={"HH-User-Agent": "Kurswork2/1.0 (andry73@yandex.ru)"},
    )


@pytest.mark.parametrize(
    "data_input, mock_result, result",
    [
        (
            "python",
            {
                "items": [
                    {
                        "id": "125426940",
                        "name": "Backend-разработчик Python/Django",
                        "salary": 250000,
                        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125426940",
                    }
                ],
                "found": 1,
                "page": 0,
                "per_page": 1,
            },
            [
                {
                    "id": "125426940",
                    "name": "Backend-разработчик Python/Django",
                    "salary": 250000,
                    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125426940",
                }
            ],
        ),
    ],
)
@patch("src.api.hh_api.HeadHunterAPI._connect_to_api")
def test_get_vacancies(mock_get, data_input, mock_result, result):
    mock_get.return_value = mock_result
    hh_api = HeadHunterAPI()
    assert hh_api.get_vacancies(data_input) == result
    mock_get.assert_called_once_with({"text": "python", "page": "0", "per_page": "100"})
