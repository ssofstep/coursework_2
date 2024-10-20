from src.hh_info import HH
from src.JSONSaver import JSONSaver
from src.utils import filter_vacancies, get_top_vacancies, print_vacancies
from src.Vacancy import Vacancy


def main() -> None:
    """Функция сборки всего проекта"""
    user_word = input("Введите слово для поиска вакансий: ")
    user_pages = int(input("Введите количество страниц (до 20) для вакансий: "))
    hh_vacancies = HH()
    hh_vacancies.load_vacancies(user_word, user_pages)
    all_vacancies = hh_vacancies.vacancies
    list_vacancies = []
    for i in all_vacancies:
        formatted_vacancy = Vacancy.vacancy_from_hh(i)
        list_vacancies.append(formatted_vacancy)
    user_filter = input("Надо отфильтровать вакансии по требованиям? [Да/Нет] ")
    if user_filter.lower().strip() == "да":
        user_filter_word = input("Введите слово, по которому необходимо выполнить фильтрацию: ")
        list_vacancies = filter_vacancies(list_vacancies, user_filter_word)
    user_top = int(input("Введите количество вакансий, которые хотите увидеть: "))
    user_sort = input("Надо ли отсортировать вакансии по зарплате? [Да/Нет] ")
    if user_sort.lower().strip() == "да":
        list_vacancies = get_top_vacancies(list_vacancies, user_top)
    else:
        list_vacancies = [list_vacancies[i] for i in range(user_top)]
    if input("Надо ли сохранять вакансии в файл? [Да/Нет] ").lower() == "да":
        name_file = input("Напишите имя файла в формате .json куда сохранять вакансии: ")
        json_saver = JSONSaver(name_file)
        for vacancy in list_vacancies:
            json_saver.add_vacancy(vacancy)
    print_vacancies(list_vacancies)


if __name__ == "__main__":
    main()
