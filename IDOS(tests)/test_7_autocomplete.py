import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import Base_Url
from config import TOP_35_CITIES


@allure.epic("IDOS.cz")
@allure.feature("Автодополнение")
@allure.story("Поле Odkud — 35 главных городов")
@allure.severity(allure.severity_level.CRITICAL)
def test_autocomplete_top_35_cities():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)  # Ожидание для стабильности

    try:
        with allure.step('Открыть сайт IDOS.cz'):
            driver.get(Base_Url)
            time.sleep(3)
            allure.attach(driver.get_screenshot_as_png(), name="страница_открыта",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step('Принять cookies (если есть)'):
            try:
                cookie_button = wait.until(EC.element_to_be_clickable((By.ID, 'didomi-notice-agree-button')))
                cookie_button.click()
                time.sleep(1)
            except TimeoutException:
                print("Баннер cookies не появился — продолжаем")  # Не падает тест

        failed = []

        with allure.step("Проверяем автодополнение для 35 городов"):
            for full_city, prefix in TOP_35_CITIES:
                with allure.step(f"Ищем: {full_city} (префикс: {prefix})"):
                    # Правильный селектор поля Odkud
                    from_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='From']")))
                    from_field.clear()
                    from_field.click()
                    time.sleep(0.5)

                    # Вводим префикс
                    from_field.send_keys(prefix)
                    time.sleep(1.5)  # Ждём AJAX-запрос

                    try:
                        # УНИВЕРСАЛЬНЫЙ селектор для выпадающего списка (div)
                        suggestion = wait.until(EC.presence_of_element_located(
                            (By.XPATH,
                             f"//div[contains(@class, 'suggestion') or contains(@class, 'idos-autosuggest') and contains(., '{prefix}')]")
                        ))

                        # Проверяем видимость и кликаем (заполняет поле полностью)
                        assert suggestion.is_displayed(), f"Элемент '{prefix}' не видим"
                        driver.execute_script("arguments[0].scrollIntoView(true);",
                                              suggestion)  # Скролл, если список длинный
                        suggestion.click()
                        time.sleep(0.5)

                        print(f"OK → {full_city}")
                        allure.attach(driver.get_screenshot_as_png(), name=f"найдено_{full_city}",
                                      attachment_type=allure.attachment_type.PNG)

                    except TimeoutException:
                        failed.append(full_city)
                        print(f"FAIL → {full_city}")
                        allure.attach(driver.get_screenshot_as_png(), name=f"НЕ_НАЙДЕНО_{full_city}",
                                      attachment_type=allure.attachment_type.PNG)

        with allure.step("Результат проверки"):
            if failed:
                allure.attach(driver.get_screenshot_as_png(), name="финальный_скрин_с_ошибками",
                              attachment_type=allure.attachment_type.PNG)
                assert False, f"Не найдены в автодополнении: {', '.join(failed)}"
            else:
                print("ВСЕ 35 ГОРОДОВ НАЙДЕНЫ!")
                allure.attach(driver.get_screenshot_as_png(), name="ВСЕ_35_ГОРОДОВ_НАЙДЕНЫ",
                              attachment_type=allure.attachment_type.PNG)

    finally:
        driver.quit()