

from src.api.hh_api import HeadHunterAPI


requ = HeadHunterAPI()
print(requ.get_vacancies("python"))
