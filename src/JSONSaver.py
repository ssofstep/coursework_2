import json
from abc import ABC, abstractmethod

from src.Vacancy import Vacancy


class Json_saver(ABC):
    """Абстрактный класс для JSONSaver"""

    @abstractmethod
    def __init__(self, filename: str):
        pass

    def add_vacancy(self, vacancy: Vacancy):
        pass

    def delete_vacancy(self, vacancy: Vacancy):
        pass


class JSONSaver:
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    def __init__(self, filename: str):
        self.__filename = filename
        with open(filename, "w", encoding="UTF8") as file:
            json.dump([], file)

    def __dump(self, item: list):
        with open(self.__filename, "w", encoding="UTF8") as file:
            json.dump(item, file)

    def add_vacancy(self, vacancy: Vacancy):
        data = {"name": vacancy.name,
                "link": vacancy.link,
                "salary": vacancy.salary,
                "requirement": vacancy.requirement}
        with open(self.__filename, "r", encoding="UTF8") as file:
            item = json.load(file)
        if data not in item:
            item.append(data)
            self.__dump(item)

    def delete_vacancy(self, vacancy: Vacancy):
        data = {"name": vacancy.name,
                "link": vacancy.link,
                "salary": vacancy.salary,
                "requirement": vacancy.requirement}
        with open(self.__filename, "r", encoding="UTF8") as file:
            item = json.load(file)
        item.remove(data)
        self.__dump(item)

    @property
    def filename(self):
        return self.__filename
