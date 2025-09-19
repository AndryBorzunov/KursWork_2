from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_storage import JsonStorage
from src.utils.filters import filter_by_solary, filter_vacancies, get_top_vacancies, sort_vacancies

# Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
# vacancy_list = hh_api.get_vacancies(
#    '{"text": "NAME:python and Удалённо", "area": "1", "page": "0", "per_page": "100"}'
# )

# Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(vacancy_list)

# Сортировка списка по зарплате
# vacancies_list.sort(key=lambda x: x.salary, reverse=True)

# Пример работы конструктора класса с одной вакансией
vacancy = Vacancy(
    {
        "id": "125270081",
        "name": "Разработчик (Python Django)",
        "salary": 300000.0,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125270081",
        "snippet": "Законченное техническое высшее образование",
    }
)

# Сохранение информации о вакансиях в файл
json_saver = JsonStorage()
json_saver.add_vacancy(vacancy.to_dict())

# Удаление вакансии
json_saver.delete_vacancy(vacancy.id_vacancy)


def print_vacancies(vacancies: list[Vacancy]) -> None:
    """Вывод вакансий человеко читаемыми строками"""
    for item in vacancies:
        print(f"Вакансия № {item.id_vacancy}")
        print(f"{item.name_vacancy}")
        print(f"Зарплата: {item.salary}")
        print(f"Ссылка на вакансию: {item.url_vacancy}")
        # print(f"Формат работы: {item.work_format}")
        print(f"Навыки: {item.snippet['Навыки']}")
        print(f"Обязанности: {item.snippet['Обязанности']}")
        print()


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    platforms = ["HeadHunter"]
    print(f"Платформа для поиска вакансий: {platforms} ")

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ").split("-")  # Пример: 100000 - 150000

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    vacancies_json = hh_api.get_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(vacancies_json)

    # Фильтрация вакансий по ключевым словам
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    # Фильтрация вакансий по зарплате
    salary_range_tuple = (float(salary_range[0]), float(salary_range[1]))
    ranged_vacancies = filter_by_solary(filtered_vacancies, salary_range_tuple)

    # Сортировка по зарплате
    ranged_vacancies = sort_vacancies(ranged_vacancies)

    # Выборка первых top_n вакансий
    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)

    # Добавление вакансий в json файл
    js = JsonStorage("data/vacancies.json")
    for item in top_vacancies:
        js.add_vacancy(item.to_dict())

    print(f"Найдено {hh_api.found_dict['found']} вакансий")

    # pprint(top_vacancies)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
