import json
from pprint import pprint
from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_storage import JsonStorage
from src.utils.filters import filter_vacancies, filter_by_solary

if __name__ == "__main__":

    hh_api = HeadHunterAPI()

    vacancy_list = hh_api.get_vacancies('{"text": "NAME:python and Удалённо", "area": "1", "page": "0", "per_page": "100"}')

    objects_list = Vacancy.cast_to_object_list(vacancy_list)

    objects_list.sort(key=lambda x: x.salary, reverse=True)

    #pprint(objects_list)

    #print(objects_list[1] < objects_list[0])

    #print(objects_list[0].salary)
    #print(objects_list[1].salary)

    #pprint(str(objects_list[0]))

    val = objects_list[0].to_dict()
    #pprint(val)

    storage = JsonStorage()
    storage.add_vacancy(val)

    storage.add_vacancy(objects_list[3].to_dict())

    #storage.delete_vacancy("125123572")

    #result = filter_vacancies(objects_list, ["блокчейне", "плазмы", "django", "sql"])

    result = filter_by_solary(objects_list, (200000, 340000))

    pprint(result)
