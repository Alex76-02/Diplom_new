import pytest
from selenium import webdriver
from page.pageui import PageUI
import allure


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.epic("ТЕСТИРОВАНИЕ UI ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_find_cyrillic_positive_ui(driver):
    find = PageUI(driver)
    with allure.step("UI. Открытие сайта Кинопоиск"):
        find.open()
    with allure.step("UI. Ожидание появления логотоипа Кинопоиск"):
        find.wait_for_logo()
    with allure.step("UI. Проверка результатов поиска фильма на кириллице"):
        result_cyrillic = find.find_cyrillic_positive_ui()
        assert result_cyrillic == "Интерстеллар"


@allure.epic("ТЕСТИРОВАНИЕ UI ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_find_latin_positive_ui(driver):
    find = PageUI(driver)
    with allure.step("UI. Открытие сайта Кинопоиск"):
        find.open()
    with allure.step("UI. Ожидание появления логотоипа Кинопоиск"):
        find.wait_for_logo()
    with allure.step("UI. Проверка результатов поиска кинофильма на латинице"):
        result_latin = find.find_latin_positive_ui()
        assert len(result_latin) > 0


@allure.epic("ТЕСТИРОВАНИЕ UI ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_find_figure_positive_ui(driver):
    find = PageUI(driver)
    with allure.step("UI. Открытие сайта Кинопоиск"):
        find.open()
    with allure.step("UI. Ожидание появления логотоипа Кинопоиск"):
        find.wait_for_logo()
    with allure.step("UI. Проверка результатов поиска кинофильма с цифрами"):
        result_figure = find.find_figure_positive_ui()
        assert result_figure == "Брат\xa02"


@allure.epic("ТЕСТИРОВАНИЕ UI ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_find_empty_negative_ui(driver):
    find = PageUI(driver)
    with allure.step("UI. Открытие сайта Кинопоиск"):
        find.open()
    with allure.step("UI. Ожидание появления логотоипа Кинопоиск"):
        find.wait_for_logo()
    with allure.step("UI. Проверка результатов пустого поиска"):
        result_empty = find.find_empty_negative_ui()
        assert result_empty is True


@allure.epic("ТЕСТИРОВАНИЕ UI ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_find_special_character_negative_ui(driver):
    find = PageUI(driver)
    with allure.step("UI. Открытие сайта Кинопоиск"):
        find.open()
    with allure.step("UI. Ожидание появления логотоипа Кинопоиск"):
        find.wait_for_logo()
    with allure.step("UI. Проверка результатов поиска со спецсимволом"):
        result_special = find.find_special_character_negative_ui()
        assert result_special == "&"


@allure.epic("ТЕСТИРОВАНИЕ UI ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_find_date_future_negative_ui(driver):
    find = PageUI(driver)
    with allure.step("UI. Открытие сайта Кинопоиск"):
        find.open()
    with allure.step("UI. Ожидание появления логотоипа Кинопоиск"):
        find.wait_for_logo()
    with allure.step("UI. Проверка результатов поиска с датой из будущего"):
        result_future = find.find_date_future_negative_ui()
        assert result_future is True


@allure.epic("ТЕСТИРОВАНИЕ UI ресурса Кинопоиск")
@allure.severity("blocker")
@pytest.mark.ui_test
def test_find_max_date_negative_ui(driver):
    find = PageUI(driver)
    with allure.step("UI. Открытие сайта Кинопоиск"):
        find.open()
    with allure.step("UI. Ожидание появления логотоипа Кинопоиск"):
        find.wait_for_logo()
    with allure.step("UI. Проверка результатов поиска в диапазоне дат"):
        result_max_date = find.find_max_date_negative_ui()
        assert len(result_max_date) > 0
