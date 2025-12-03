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

@allure.title("Проверка сообщений при неправильном логине и пароле на IDOS.cz")
@allure.description("Тест проверяет 4 сценария: неправильный пароль, неправильный email, пустое поле email и пустое поле пароля.")
def test_incorrect_password(driver):
    with allure.step('Открыть сайт IDOS.cz'):
        driver.get(Base_Url)
        time.sleep(3)

    with allure.step('Принять cookies'):
        driver.find_element(By.ID, 'didomi-notice-agree-button').click()
        time.sleep(1)

    with (allure.step('Попытка входа с неправильным паролем')):
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login")
            login_button.click()
            time.sleep(1)

            email = driver.find_element(By.ID, 'Email')
            email.send_keys('none@email.com')

            password = driver.find_element(By.ID, 'Password')
            password.send_keys('12345')

            submit = driver.find_element(By.XPATH, "//div[@class='submit']")
            submit.click()
            time.sleep(5)

            message = driver.find_element(By.XPATH, "//p[@class='error']").text
            assert message == 'Chybně zadaný e-mail nebo heslo.', f"Ожидалось сообщение о неправильном пароле, но получено: {message}"


        except NoSuchElementException:
            allure.attach("Не удалось найти элемент при вводе неправильного пароля", "Ошибка",
                          allure.attachment_type.TEXT)
            pytest.fail("Не удалось выполнить проверку неправильного пароля")




def test_incorrect_email(driver):
    with allure.step('Открыть сайт IDOS.cz'):
        driver.get('https://idos.cz/vlakyautobusymhdvse/spojeni/')
        time.sleep(3)

    with allure.step('Принять cookies'):
        driver.find_element(By.ID, 'didomi-notice-agree-button').click()
        time.sleep(1)

    with allure.step('Попытка входа с неправильным email'):
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login")
            login_button.click()
            time.sleep(1)

            email = driver.find_element(By.ID, 'Email')
            email.send_keys('noneEmail.com')

            password = driver.find_element(By.ID, 'Password')
            password.send_keys('Q123458*hyhg')

            submit = driver.find_element(By.XPATH, "//div[@class='submit']")
            submit.click()
            time.sleep(5)

            message = driver.find_element(By.CLASS_NAME, 'inp-combined.filled.error').text
            assert message == 'E-MAILE-mailová adresa má chybný formát', f"Ожидалось сообщение о неправильном формате email, но получено: {message}"

        except NoSuchElementException:
            allure.attach("Не удалось найти элемент при вводе неправильного формата email", "Ошибка",
            allure.attachment_type.TEXT)
            pytest.fail("Не удалось выполнить проверку неправильного формата email")


def test_empty_email_field(driver):
    with allure.step('Открыть сайт IDOS.cz'):
        driver.get('https://idos.cz/vlakyautobusymhdvse/spojeni/')
        time.sleep(3)

    with allure.step('Принять cookies'):
        driver.find_element(By.ID, 'didomi-notice-agree-button').click()
        time.sleep(1)

    with allure.step('Попытка входа с пустым полем email'):
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login")
            login_button.click()
            time.sleep(1)

            email = driver.find_element(By.ID, 'Email')
            email.send_keys('')

            password = driver.find_element(By.ID, 'Password')
            password.send_keys('Q123458*hyhg')

            submit = driver.find_element(By.XPATH, "//div[@class='submit']")
            submit.click()
            time.sleep(5)

            message = driver.find_element(By.CLASS_NAME, 'inp-combined.error').text
            assert message == 'E-MAILZadejte e-mail', f"Ожидалось сообщение 'введите email', но получено: {message}"

        except NoSuchElementException:
            allure.attach("Не удалось найти элемент при входе с пустым полем email", "Ошибка",
            allure.attachment_type.TEXT)
            pytest.fail("Не удалось выполнить проверку при входе с пустым полем email")



def test_empty_password_field(driver):
    with allure.step('Открыть сайт IDOS.cz'):
        driver.get('https://idos.cz/vlakyautobusymhdvse/spojeni/')
        time.sleep(3)

    with allure.step('Принять cookies'):
        driver.find_element(By.ID, 'didomi-notice-agree-button').click()
        time.sleep(1)

    with allure.step('Попытка входа с пустым полем пароля'):
        try:
            login_button = driver.find_element(By.CLASS_NAME, "login")
            login_button.click()
            time.sleep(1)

            email = driver.find_element(By.ID, 'Email')
            email.send_keys('none@email.com')

            password = driver.find_element(By.ID, 'Password')
            password.clear()

            submit = driver.find_element(By.XPATH, "//div[@class='submit']")
            submit.click()
            time.sleep(5)

            message = driver.find_element(By.CLASS_NAME, 'inp-combined.error').text
            assert message == "HESLOZadejte heslo", f"Ожидалось сообщение 'введите пароль ', но получено: '{message}'"

        except NoSuchElementException:
            allure.attach("Не удалось найти элемент при входе с пустым полем пароля", "Ошибка",
            allure.attachment_type.TEXT)
            pytest.fail("Не удалось выполнить проверку попытки входа с пустым полем пароля")