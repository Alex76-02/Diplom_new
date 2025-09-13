from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PageUI:
    """
    Класс страницы поиска
    """
    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.CLASS_NAME, "kinopoisk-header-logo__img")
        self.url = "https://www.kinopoisk.ru/"

    def open(self):
        """
        Открытие браузера
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        return self

    def wait_for_logo(self, timeout=40):
        """
        Ожидание открытия страницы (появление логотипа Кинопоиск)
        """
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.logo)
        )
        return self

    def find_cyrillic_positive_ui(self) -> str:
        """
        Функция поиска контента на кириллице
        """

        self.driver.find_element(By.NAME, "kp_query").click()
        self.driver.find_element(By.NAME, "kp_query").send_keys(
            "Интерстеллар"
            )
        self.driver.find_element(By.NAME, "kp_query").send_keys(Keys.RETURN)
        """
        Ожидание результатов поиска
        """
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flap_img"))
            )
        """
        Обработка результатов поиска
        """
        res_list = self.driver.find_elements(By.CSS_SELECTOR, ".flap_img")
        res = res_list[0].get_attribute("alt")
        return res

    def find_latin_positive_ui(self) -> list:
        """
        Функция поиска контента на латинице
        """
        self.driver.find_element(By.NAME, "kp_query").click()
        self.driver.find_element(By.NAME, "kp_query").send_keys(
            "Wrath of Man"
            )
        self.driver.find_element(By.NAME, "kp_query").send_keys(Keys.RETURN)
        """
        Ожидание результатов поиска
        """
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, "//*[text()='Wrath of Man']")
            ))
        """
        Обработка результатов поиска
        """
        res_list = self.driver.find_elements(
            By.XPATH, "//*[text()='Wrath of Man']"
            )
        return res_list

    def find_figure_positive_ui(self) -> str:
        """
        Функция поиска контента с цифрами в названии
        """
        self.driver.find_element(By.NAME, "kp_query").click()
        self.driver.find_element(By.NAME, "kp_query").send_keys("Брат 2")
        self.driver.find_element(By.NAME, "kp_query").send_keys(Keys.RETURN)
        """
        Ожидание результатов поиска
        """
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flap_img"))
            )
        """
        Обработка результатов поиска
        """
        res_list = self.driver.find_elements(By.CSS_SELECTOR, ".flap_img")
        res = res_list[0].get_attribute("alt")
        return res

    def find_empty_negative_ui(self) -> object:
        """
        Функция поиска контента с пустым названием
        """
        self.driver.find_element(By.NAME, "kp_query").click()
        self.driver.find_element(By.NAME, "kp_query").send_keys(Keys.RETURN)
        """
        Ожидание результатов поиска (ожидаем, что ничего не нашлось)
        """
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#search"))
            )
        """
        Обработка результатов поиска, проверяем баннер с предложением выбрать
        случайный фильм
        """
        res_button = self.driver.find_element(
            By.CSS_SELECTOR, "#search"
            ).is_enabled()
        return res_button

    def find_special_character_negative_ui(self) -> str:
        """
        Функция поиска контента со спецсимволом в названии
        """
        self.driver.find_element(By.NAME, "kp_query").click()
        self.driver.find_element(By.NAME, "kp_query").send_keys("&")
        self.driver.find_element(By.NAME, "kp_query").send_keys(Keys.RETURN)
        """
        Ожидание результатов поиска
        """
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flap_img"))
            )
        """
        Обработка результатов поиска
        """
        res_list = self.driver.find_elements(By.CSS_SELECTOR, ".flap_img")
        res = res_list[0].get_attribute("alt")
        return res

    def find_date_future_negative_ui(self) -> str:
        """
        Функция поиска контента с датой выпуска из будущего (2100 год)
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "[aria-label='Расширенный поиск']"
            ).click()
        self.driver.find_element(By.CSS_SELECTOR, "#year").send_keys("2100")
        self.driver.find_element(
            By.CSS_SELECTOR, ".el_18.submit.nice_button"
            ).click()
        """
        Ожидание результатов поиска (ожидаем, что ничего не нашлось)
        """
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".textorangebig"))
            )
        """
        Обработка результатов поиска, проверяем, что появилась надпись
        'К сожалению, по вашему запросу ничего не найдено...'
        """
        res = self.driver.find_element(
            By.CSS_SELECTOR, ".textorangebig"
            ).is_enabled()
        return res

    def find_max_date_negative_ui(self) -> list:
        """
        Функция поиска контента с датой выпуска из дипазона дат + название
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "[aria-label='Расширенный поиск']"
            ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#find_film"
            ).send_keys("Брат")
        self.driver.find_element(
            By.CSS_SELECTOR, "#from_year"
            ).send_keys("2020")
        self.driver.find_element(
            By.CSS_SELECTOR, "#to_year"
            ).send_keys("2026")
        self.driver.find_element(
            By.CSS_SELECTOR, ".el_18.submit.nice_button"
            ).click()
        """
        Ожидание результатов поиска (ожидаем, что ничего не нашлось)
        """
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='Брат']"))
            )
        """
        Обработка результатов поиска
        """
        res_list = self.driver.find_elements(By.XPATH, "//*[text()='Брат']")
        return res_list
