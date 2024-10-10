from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword, pages=20):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword, pages=20):
        self.params['text'] = keyword
        while self.params.get('page') != pages:
            print("start")
            response = requests.get(self.url, headers=self.headers, params=self.params)
            print(response.status_code)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
