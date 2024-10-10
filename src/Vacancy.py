class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, name: str, link: str, salary: float, requirement: str):
        self.name = name
        self.link = link
        self.salary = salary
        self.requirement = requirement
        self.validation()

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def validation(self):
        if self.salary is None:
            self.salary = 0.0
