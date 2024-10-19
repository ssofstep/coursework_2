class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, name: str, link: str, salary: float, requirement: str):
        self.__name = name
        self.__link = link
        self.__salary = salary
        self.__requirement = requirement
        self.__validation()

    @property
    def salary(self):
        return self.__salary

    @property
    def name(self):
        return self.__name

    @property
    def link(self):
        return self.__link

    @property
    def requirement(self):
        return self.__requirement

    def __lt__(self, other: 'Vacancy'):
        return self.__salary < other.salary

    def __le__(self, other: 'Vacancy'):
        return self.__salary <= other.salary

    def __validation(self):
        if self.__salary is None:
            self.__salary = 0.0

        if self.__requirement is None:
            self.__requirement = "NotFound"

    def __str__(self):
        return (f"Имя вакансии: {self.__name}, ссылка: {self.__link}, зарплата: {self.__salary}, требование: "
                f"{self.__requirement}")

    @classmethod
    def vacancy_from_hh(cls, data: dict) -> 'Vacancy':
        salary = data.get("salary")
        if salary is not None:
            if salary.get("to") is None:
                salary = salary.get("from")
            else:
                salary = salary.get("to")
        requirement = data.get("snippet")
        if requirement is not None:
            requirement = requirement.get("requirement")
        return cls(name=data.get("name", "NotFound"),
                   link=data.get("alternate_url", "error"),
                   salary=salary,
                   requirement=requirement)
