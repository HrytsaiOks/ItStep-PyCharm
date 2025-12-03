import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from config import Base_Url

@pytest.fixture(scope="function")
def driver():
    """Инициализация браузера"""
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.title("Поиск маршрута с некорректными данными 'xxxzzz' и спецсимволами '#$%'")
@allure.description(
    "Тест проверяет, что сайт IDOS.cz корректно обрабатывает ввод несуществующих станций и выдаёт сообщение об ошибке или пустой результат."
)
def test_search_invalid_data1(driver):
    with allure.step("Открыть сайт IDOS.cz"):
        driver.get(Base_Url)
        time.sleep(3)

    with allure.step("Принять cookies"):
        try:
            driver.find_element(By.ID, "didomi-notice-agree-button").click()
            time.sleep(1)
        except:
            pass

    with allure.step("Ввод некорректных данных, несуществующего города 'xxxzzz' и нажатие поиска"):
        field_from = driver.find_element(By.XPATH, "//*[@id='From']")
        field_to = driver.find_element(By.XPATH, "//*[@id='To']")

        field_from.clear()
        field_from.send_keys("xxxzzz")

        field_to.clear()
        field_to.send_keys("xxxzzz")

        search_button = driver.find_element(By.CSS_SELECTOR, "#connection-filter > div.submit > button")
        search_button.click()
        time.sleep(3)

    with allure.step("Проверка, что сайт отобразил ошибку или пустой результат"):
        try:

            error_elements = driver.find_elements(By.CSS_SELECTOR, ".error, .alert")
            result_elements = driver.find_elements(By.CSS_SELECTOR, ".connection")

            assert len(error_elements) > 0 or len(result_elements) == 0, \
                "Ожидалась ошибка или пустой результат для некорректных станций, но найден результат."

            for el in error_elements:
                allure.attach(el.text, "Сообщение об ошибке", allure.attachment_type.TEXT)
                print("Сообщение об ошибке:", el.text)

            if len(result_elements) == 0:
                print("✓ Результаты отсутствуют, как и ожидалось.")

        except NoSuchElementException:
            allure.attach("Элемент с ошибкой не найден", "Ошибка", allure.attachment_type.TEXT)
            pytest.fail("Поиск с некорректными данными прошёл без ошибок, что некорректно.")

def test_search_invalid_data2(driver):
    with allure.step("Открыть сайт IDOS.cz"):
        driver.get(Base_Url)
        time.sleep(3)

    with allure.step("Принять cookies"):
        try:
            driver.find_element(By.ID, "didomi-notice-agree-button").click()
            time.sleep(1)
        except:
            pass

    with allure.step("Ввод спецсимволов '#$%' и нажатие поиска"):
        field_from = driver.find_element(By.XPATH, "//*[@id='From']")
        field_to = driver.find_element(By.XPATH, "//*[@id='To']")

        field_from.clear()
        field_from.send_keys("#$%")

        field_to.clear()
        field_to.send_keys("#$%")

        search_button = driver.find_element(By.CSS_SELECTOR, "#connection-filter > div.submit > button")
        search_button.click()
        time.sleep(3)

    with allure.step("Проверка, что сайт отобразил ошибку или пустой результат"):
        try:

            error_elements = driver.find_elements(By.CSS_SELECTOR, ".error, .alert")
            result_elements = driver.find_elements(By.CSS_SELECTOR, ".connection")

            assert len(error_elements) > 0 or len(result_elements) == 0, \
                "Ожидалась ошибка или пустой результат при вводе спецсимволов, но найден результат."

            for el in error_elements:
                allure.attach(el.text, "Сообщение об ошибке", allure.attachment_type.TEXT)
                print("Сообщение об ошибке:", el.text)

            if len(result_elements) == 0:
                print("✓ Результаты отсутствуют, как и ожидалось.")

        except NoSuchElementException:
            allure.attach("Элемент с ошибкой не найден", "Ошибка", allure.attachment_type.TEXT)
            pytest.fail("Поиск при вводе спецсимволов прошёл без ошибок, что некорректно.")
