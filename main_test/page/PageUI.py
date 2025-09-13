from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PageUI:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.kinopoisk.ru/")
        self._driver.maximize_window()

    def find_cyrillic_positive_ui(self):

        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).send_keys("Интерстеллар")
        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).send_keys(Keys.RETURN)

        WebDriverWait(self._driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flap_img"))
            )

        res_list = self._driver.find_elements(By.CSS_SELECTOR, ".flap_img")
        res = res_list[0].get_attribute("alt")
        return res

    def find_latin_positive_ui(self):
        self._driver.maximize_window()
        self._driver.get("https://www.kinopoisk.ru/")

        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).send_keys("Wrath of Man")
        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).send_keys(Keys.RETURN)

        WebDriverWait(self._driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, "//*[text()='Wrath of Man']")
            ))

        res_list = self._driver.find_elements(
            By.XPATH, "//*[text()='Wrath of Man']"
            )
        return res_list

    def find_figure_positive_ui(self):
        self._driver.maximize_window()
        self._driver.get("https://www.kinopoisk.ru/")

        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).send_keys("Брат 2")
        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).send_keys(Keys.RETURN)

        WebDriverWait(self._driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flap_img"))
            )

        res_list = self._driver.find_elements(By.CSS_SELECTOR, ".flap_img")
        res = res_list[0].get_attribute("alt")
        return res

    def find_empty_negative_ui(self):
        self._driver.maximize_window()
        self._driver.get("https://www.kinopoisk.ru/")

        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).send_keys(Keys.RETURN)

        WebDriverWait(self._driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#search"))
            )

        res_button = self._driver.find_element(
            By.CSS_SELECTOR, "#search"
            ).is_enabled()
        return res_button

    def find_special_character_negative_ui(self):
        self._driver.maximize_window()
        self._driver.get("https://www.kinopoisk.ru/")

        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).send_keys("&")
        self._driver.find_element(
            By.CSS_SELECTOR, ".styles_inputActive__mIqMs"
            ).send_keys(Keys.RETURN)

        WebDriverWait(self._driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flap_img"))
            )

        res_list = self._driver.find_elements(By.CSS_SELECTOR, ".flap_img")
        res = res_list[0].get_attribute("alt")
        return res

    def find_date_future_negative_ui(self):
        self._driver.maximize_window()
        self._driver.get("https://www.kinopoisk.ru/")

        self._driver.find_element(
            By.CSS_SELECTOR, "[aria-label='Расширенный поиск']"
            ).click()
        self._driver.find_element(By.CSS_SELECTOR, "#year").send_keys("2100")
        self._driver.find_element(
            By.CSS_SELECTOR, ".el_18.submit.nice_button"
            ).click()

        WebDriverWait(self._driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".textorangebig"))
            )

        res = self._driver.find_element(
            By.CSS_SELECTOR, ".textorangebig"
            ).is_enabled()
        return res

    def find_max_date_negative_ui(self):
        self._driver.maximize_window()
        self._driver.get("https://www.kinopoisk.ru/")

        self._driver.find_element(
            By.CSS_SELECTOR, "[aria-label='Расширенный поиск']"
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#find_film"
            ).send_keys("Брат")
        self._driver.find_element(
            By.CSS_SELECTOR, "#from_year"
            ).send_keys("2020")
        self._driver.find_element(
            By.CSS_SELECTOR, "#to_year"
            ).send_keys("2026")
        self._driver.find_element(
            By.CSS_SELECTOR, ".el_18.submit.nice_button"
            ).click()

        WebDriverWait(self._driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='Брат']"))
            )

        res_list = self._driver.find_elements(By.XPATH, "//*[text()='Брат']")
        return res_list
