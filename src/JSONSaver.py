import json

from src.Vacancy import Vacancy


class JSONSaver:
    """Класс для сохранения информации о вакансиях в JSON-файл"""
    def __init__(self, filename: str):
        self.filename = filename
        with open(filename, "w", encoding="UTF8") as file:
            json.dump([], file)

    def add_vacancy(self, vacancy: Vacancy):
        data = {"name": vacancy.name,
                "link": vacancy.link,
                "salary": vacancy.salary,
                "requirement": vacancy.requirement}
        with open(self.filename, "r", encoding="UTF8") as file:
            item = json.load(file)
        if data not in item:
            item.append(data)
            with open(self.filename, "w", encoding="UTF8") as file:
                json.dump(item, file)
