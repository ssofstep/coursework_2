from src.Vacancy import Vacancy


def get_top_vacancies(vacancies: list[Vacancy], n: int) -> list:
    vacancies.sort()
    new_list = []
    for i in range(n):
        new_list.append(vacancies[i])
    return new_list


def filter_vacancies(vacancies: list[Vacancy], filter_word: str) -> list:
    new_list = []
    for i in vacancies:
        if filter_word in i.requirement:
            new_list.append(i)

    return new_list


def print_vacancies(vacancies: list[Vacancy]) -> None:
    for i in vacancies:
        print(i)
