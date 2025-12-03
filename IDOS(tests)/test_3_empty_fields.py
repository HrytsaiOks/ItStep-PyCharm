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
    # options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

@allure.title("Поиск маршрута без заполнения полей 'Odkud / Kam'")
@allure.description(
    "Тест проверяет, что сайт IDOS.cz не выполняет поиск маршрута, если поля 'Odkud' и 'Kam' пустые, "
    "и выдаёт соответствующее сообщение об ошибке.")
def test_search_empty_fields(driver):
    with allure.step("Открыть сайт IDOS.cz"):
        driver.get(Base_Url)
        time.sleep(3)

    with allure.step('Принять cookies'):
        driver.find_element(By.ID, 'didomi-notice-agree-button').click()
        time.sleep(1)

    with allure.step("Оставляем поля 'Odkud / Kam' пустыми и нажимаем 'Hledat'"):
        search_button = driver.find_element(By.CSS_SELECTOR, "#connection-filter > div.submit > button")
        search_button.click()
        time.sleep(2)

    with allure.step("Проверяем, что появилась ошибка или поиск не выполнен"):
        try:
            error_elements1 = driver.find_element(By.CLASS_NAME, "inp-combined.with-map.error").text
            assert error_elements1 == 'ODKUD Vyberte místo odkud chcete cestovat', f"Ожидалось сообщение о том, что нужно заполнить поле, но получено: {message}"

            error_elements2 = driver.find_element(By.CSS_SELECTOR, "#connection-filter > div.from-to > div > div:nth-child(2)").text
            assert error_elements2 == 'KAM Vyberte místo kam chcete cestovat', f"Ожидалось сообщение о том, что нужно заполнить поле, но получено: {message}"

        except NoSuchElementException:
            allure.attach("Элемент с ошибкой не найден", "Ошибка", allure.attachment_type.TEXT)
            pytest.fail("Поиск прошёл без заполнения полей, но сообщение об ошибке отсутствует.")


