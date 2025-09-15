import requests
import pytest
from constants import BASE_URL, API_KEY
import allure

headers = {
    "X-API-KEY": API_KEY,
    "accept": 'application/json'
    }


@allure.epic("ТЕСТИРОВАНИЕ API ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.api_test
def test_find_cyrillic_positive_api():
    """
    Функция поиска контента на кириллице
    """
    with allure.step("API. Формирование URL"):
        base_url_loc = BASE_URL + "/search?page=1&limit=10&query=Интерстеллар"
    with allure.step("API. Формирование запроса - поиск на кириллице"):
        response = requests.get(base_url_loc, headers=headers)
    with allure.step("API. Проверка статуса"):
        assert response.status_code == 200


@allure.epic("ТЕСТИРОВАНИЕ API ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.api_test
def test_find_latin_positive_api():
    """
    Функция поиска контента на латинице
    """
    with allure.step("API. Формирование URL"):
        base_url_loc = BASE_URL + "/search?page=1&limit=10&query=Wrath of Man"
    with allure.step("API. Формирование запроса - поиск на латинице"):
        response = requests.get(base_url_loc, headers=headers)
    with allure.step("API. Проверка статуса"):
        assert response.status_code == 200


@allure.epic("ТЕСТИРОВАНИЕ API ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.api_test
def test_find_figure_positive_api():
    """
    Функция поиска контента с цифрами
    """
    with allure.step("API. Формирование URL"):
        base_url_loc = BASE_URL + "/search?page=1&limit=10&query=Брат 2"
    with allure.step("API. Формирование запроса - поиск с цифрами в названии"):
        response = requests.get(base_url_loc, headers=headers)
    with allure.step("API. Проверка статуса"):
        assert response.status_code == 200


@allure.epic("ТЕСТИРОВАНИЕ API ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.api_test
def test_find_empty_negative_api():
    """
    Функция поиска контента с пустым названием
    """
    with allure.step("API. Формирование URL"):
        base_url_loc = BASE_URL + "?page=1&limit=10&selectFields=id"
        "&selectFields=name&sortField=name&sortType=1&name=null"
    with allure.step("API. Формирование запроса - пустой поиск"):
        response = requests.get(base_url_loc, headers=headers)
    with allure.step("API. Проверка статуса"):
        assert response.status_code == 200


@allure.epic("ТЕСТИРОВАНИЕ API ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.api_test
def test_find_special_character_negative_api():
    """
    Функция поиска контента со спецсимволами
    """
    with allure.step("API. Формирование URL"):
        base_url_loc = BASE_URL + "?page=1&limit=10&selectFields=id"
        "&selectFields=name&sortField=name&sortType=1&name=#"
    with allure.step("API. Формирование запроса - поиск со спецсимволами"):
        response = requests.get(base_url_loc, headers=headers)
    with allure.step("API. Проверка статуса"):
        assert response.status_code == 200


@allure.epic("ТЕСТИРОВАНИЕ API ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.api_test
def test_find_date_future_negative_api():
    """
    Функция поиска контента с датой выпуска из будущего
    """
    with allure.step("API. Формирование URL"):
        base_url_loc = BASE_URL + "?page=1&limit=10&selectFields=name"
        "&selectFields=year&notNullFields=name&notNullFields=year&year=2100"
    with allure.step("API. Формирование запроса - поиск с датой из будущего"):
        response = requests.get(base_url_loc, headers=headers)
    with allure.step("API. Проверка статуса"):
        assert response.status_code == 200


@allure.epic("ТЕСТИРОВАНИЕ API ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.api_test
def test_find_max_date_negative_api():
    """
    Функция поиска контента в диапазоне дат + наименование
    """
    with allure.step("API. Формирование URL"):
        base_url_loc = BASE_URL + "?page=1&limit=10&selectFields=name"
        "&selectFields=year&notNullFields=name&notNullFields=year&"
        "sortField=year&sortType=1&year=2000-2028"
    with allure.step("API. Формирование запроса - поиск по диапазону дат"):
        response = requests.get(base_url_loc, headers=headers)
    with allure.step("API. Проверка статуса"):
        assert response.status_code == 200
