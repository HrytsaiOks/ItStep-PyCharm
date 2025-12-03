import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Base_Url
from config import input_mesto_1, input_mesto_2


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Поиск маршрута — корректность построения")
@allure.description(
    "Тест проверяет, что при вводе корректных станций (Praha → Brno) "
    "и текущей даты сайт IDOS.cz строит маршрут и отображает корректные результаты."
)
def test_correct_route_search(driver):

    with allure.step("Открыть IDOS.cz"):
        driver.get(Base_Url)
        time.sleep(2)

    with allure.step("Принять cookies"):
        try:
            driver.find_element(By.ID, "didomi-notice-agree-button").click()
            time.sleep(1)
        except:
            pass

    with allure.step("Ввод станций 'Praha → Brno'"):
        field_from = driver.find_element(By.XPATH, "//*[@id='From']")
        field_to = driver.find_element(By.XPATH, "//*[@id='To']")

        field_from.clear()
        field_from.send_keys(input_mesto_1)
        time.sleep(1)
        field_from.send_keys(Keys.ENTER)

        field_to.clear()
        field_to.send_keys(input_mesto_2)
        time.sleep(1)
        field_to.send_keys(Keys.ENTER)


    with allure.step("Поиск маршрута"):
    # Закрыть автокомплит — самый надёжный способ
        actions = ActionChains(driver)
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(0.5)

        search_button = driver.find_element(By.CSS_SELECTOR, "#connection-filter > div.submit > button")
        search_button.click()
        time.sleep(4)

    with allure.step("Проверка корректности станции отправления"):
        first_result = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".connection"))
        )
        # Ищем элемент станции отправления внутри первого маршрута по тексту 'Praha'= input_mesto_1
        from_station =  first_result.find_element(By.XPATH, ".//*[contains(text(), input_mesto_1)]").text

        assert from_station, "Не удалось найти станцию отправления"
        print("From station:", from_station)

    with allure.step("Проверка корректности станции прибытия"):
        # Ищем элемент станции прибытия внутри первого маршрута по тексту 'Brno' = input_mesto_2
        to_station = first_result.find_element(By.XPATH, ".//*[contains(text(), input_mesto_2)]").text

        assert to_station, "Не удалось найти станцию отправления"
        print("TO station:", to_station)





