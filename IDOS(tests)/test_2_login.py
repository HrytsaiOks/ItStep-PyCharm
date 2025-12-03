import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from config import *

@pytest.fixture(scope="function")
def driver():
    """Инициализация браузера"""
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@allure.title("Вход зарегистрированого пользователя на IDOS.cz")
@allure.description("Тест проверяет вход зарегистрированого пользователя на IDOS.cz.")
def test_incorrect_password(driver):
    with allure.step('Открыть сайт IDOS.cz'):
        driver.get(Base_Url)
        time.sleep(3)

    with allure.step('Принять cookies'):
        driver.find_element(By.ID, 'didomi-notice-agree-button').click()
        time.sleep(1)

    with (allure.step('Совершаем вход с правильным паролем и email, проверяем имя зарегистрированого пользователя')):
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login")
            login_button.click()
            time.sleep(1)

            email = driver.find_element(By.ID, 'Email')
            email.send_keys(input_email)

            password = driver.find_element(By.ID, 'Password')
            password.send_keys(input_password)

            submit = driver.find_element(By.XPATH, "//div[@class='submit']")
            submit.click()
            time.sleep(5)

            message = driver.find_element(By.XPATH, "//*[@id='header']/div[1]/p/a[1]").text
            assert message == user_name, f"Ожидалось сообщение о неправильном имени зарегистрированного пользователя, но получено: {message}"
            print(message)

        except NoSuchElementException:
            allure.attach("Не удалось найти элемент при вводе правильного пароля и эмейла", "Ошибка",
                          allure.attachment_type.TEXT)
            pytest.fail("Не удалось выполнить проверку входа зарегистрированного пользователя")
