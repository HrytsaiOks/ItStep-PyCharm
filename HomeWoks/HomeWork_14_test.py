import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import allure

input_first_name = 'Margaryta'
input_last_name = 'Zajko'
input_user_name = 'Margo*777*'
input_password = 'Qazokm123*'

def open_web(driver, link):
    with allure.step("Открываем страницу с формой регистрации"):
        driver.get(link)

@allure.feature('Форма регистрации')
@allure.story('Заполнение формы регистрации')

def test_fill_Registration_form():
    with allure.step("Создаем драйвер"):
        driver = webdriver.Chrome()
    try:
        open_web(driver, 'https://demoqa.com/login')
        with allure.step('Нажимаем на кнопку New User.'):
            click_button_new_user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'newUser')))
            driver.execute_script("arguments[0].scrollIntoView(true);", click_button_new_user )
            click_button_new_user .click()
            time.sleep(5)

        with allure.step('Заполняем поля формы регистрации'):
            first_name = driver.find_element(By.ID, "firstname")
            first_name.send_keys(input_first_name)

            last_name = driver.find_element(By.ID, "lastname")
            last_name.send_keys(input_last_name)

            user_name = driver.find_element(By.ID, "userName")
            user_name.send_keys(input_user_name)

            password = driver.find_element(By.ID, "password")
            password.send_keys(input_password)

        with allure.step('❗Ждем ручного подтверждения капчи (25 сек)'):
            print("Подтверди капчу вручную в течение 25 секунд...")
            time.sleep(25)

        with allure.step('Отправляем форму регистрации'):
            click_button_register = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'register')))
            driver.execute_script("arguments[0].scrollIntoView(true);", click_button_register)
            time.sleep(0.5)
            click_button_register.click()
            time.sleep(5)

        with allure.step("Проверяем, что регистрация прошла успешно"):
             WebDriverWait(driver, 10).until(EC.alert_is_present())
             alert = driver.switch_to.alert

             alert_text = alert.text
             print(f"✅ Alert appeared: {alert_text}")
             assert "User Register Successfully." in alert_text, "❌ Не то сообщение в alert!"

        alert.accept()
        print("✅ Alert accepted.")

    except NoAlertPresentException:
        raise AssertionError("❌ Alert с сообщением о регистрации не появился.")

    finally:
        with allure.step('Закрываем драйвер'):
            driver.quit()



def open_web(driver, link):
    with allure.step("Открываем страницу с формой регистрации"):
        driver.get(link)

@allure.feature('Форма регистрации')
@allure.story('Позитивный тест логина')

def test_positive_login():
    with allure.step("Создаем драйвер"):
        driver = webdriver.Chrome()
    try:
        open_web(driver, 'https://demoqa.com/login')
        with allure.step('Вводим логин и пароль только что зарегистрированного пользователя.'):

            user_name = driver.find_element(By.ID, "userName")
            user_name.send_keys(input_user_name)

            password = driver.find_element(By.ID, "password")
            password.send_keys(input_password)

        with allure.step('Нажимаем на кнопку Login.'):

            click_button_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login')))
            driver.execute_script("arguments[0].scrollIntoView(true);", click_button_login)
            click_button_login.click()
            time.sleep(5)

        with allure.step('Проверяем произошёл ли переход на страницу https://demoqa.com/profile.'):

            WebDriverWait(driver, 5).until(EC.url_to_be("https://demoqa.com/profile"))
            current_url = driver.current_url
            assert current_url == "https://demoqa.com/profile", \
                f"❌ Expected to be on profile page, but got: {current_url}"

    finally:
        with allure.step('Закрываем драйвер'):
            driver.quit()


def open_web(driver, link):
    with allure.step("Открываем страницу driver.get(link)"):
        driver.get(link)

@allure.feature('Форма регистрации')
@allure.story('Негативный тест логина')

def test_negative_login():
    with allure.step("Создаем драйвер"):
        driver = webdriver.Chrome()
    try:
        open_web(driver, 'https://demoqa.com/login')
        with allure.step('Вводим логин и неверный пароль только что зарегистрированного пользователя.'):

            userName_input = driver.find_element(By.ID, "userName")
            userName_input.send_keys(input_user_name)

            password_wrong = driver.find_element(By.ID, "password")
            password_wrong.send_keys('Qazokm12345')

        with allure.step('Нажимаем на кнопку Login.'):

            click_button_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login')))
            driver.execute_script("arguments[0].scrollIntoView(true);", click_button_login)
            click_button_login.click()
            time.sleep(5)

        with allure.step('Проверяем, что отображается ошибка (например: Invalid username or password!)..'):
            error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))
            assert "Invalid username or password!" in error_message.text, \
                f"❌ Unexpected error message: {error_message.text}"
    finally:
        with allure.step('Закрываем драйвер'):
            driver.quit()


