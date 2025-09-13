import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from page.PageUI import PageUI
# import allure


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
        )
    yield driver
    driver.quit()


def test_find_cyrillic_positive_ui(driver):
    find = PageUI(driver)
    result_cyrillic = find.find_cyrillic_positive_ui()
    assert result_cyrillic == "Интерстеллар"


def test_find_latin_positive_ui(driver):
    find = PageUI(driver)
    result_latin = find.find_latin_positive_ui()
    assert len(result_latin) > 0


def test_find_figure_positive_ui(driver):
    find = PageUI(driver)
    result_figure = find.find_figure_positive_ui()
    assert result_figure == "Брат\xa02"


def test_find_empty_negative_ui(driver):
    find = PageUI(driver)
    result_empty = find.find_empty_negative_ui()
    assert result_empty is True


def test_find_special_character_negative_ui(driver):
    find = PageUI(driver)
    result_special = find.find_special_character_negative_ui()
    assert result_special == "&"


def test_find_date_future_negative_ui(driver):
    find = PageUI(driver)
    result_future = find.find_date_future_negative_ui()
    assert result_future is True


def test_find_max_date_negative_ui(driver):
    find = PageUI(driver)
    result_max_date = find.find_max_date_negative_ui()
    assert len(result_max_date) > 0
