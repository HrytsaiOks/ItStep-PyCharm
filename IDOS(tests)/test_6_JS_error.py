import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from config import Base_Url


# Домены рекламы, которые нужно игнорировать
IGNORED_DOMAINS = [
    "doubleclick.net", "googlesyndication.com", "googleadservices.com",
    "googletagmanager.com", "adnxs.com", "adsafeprotected.com",
    "adform.net", "33across.com", "cdn-ima.33across.com",
    "rubiconproject.com", "fastlane.rubiconproject.com",
    "pubmatic.com", "criteo.com", "seznam.cz", "imrworldwide.com"
]


@pytest.fixture
def driver():
    """Запуск браузера с включёнными логами JS."""
    options = webdriver.ChromeOptions()
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()


@allure.title("Проверка консоли браузера на наличие реальных JS ошибок")
@allure.description("Тест фиксирует только ошибки сайта IDOS и игнорирует ошибки рекламных скриптов.")
def test_js_console_errors(driver):

    with allure.step("Открываем IDOS.cz"):
        driver.get(Base_Url)
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), "page_load", allure.attachment_type.PNG)

    with allure.step("Принимаем cookies (если есть)"):
        try:
            driver.find_element(By.ID, "didomi-notice-agree-button").click()
            time.sleep(1)
        except:
            pass

    with allure.step("Ждём 10 сек — загрузка всей рекламы"):
        time.sleep(10)

    with allure.step("Получаем логи JS из браузера"):
        logs = driver.get_log("browser")
        allure.attach(str(logs), "raw_browser_log", allure.attachment_type.TEXT)

    with allure.step("Фильтрация ошибок: только реальные ошибки сайта"):
        real_errors = []

        for entry in logs:
            level = entry.get("level")
            msg = entry.get("message").lower()

            # берём только ошибки
            if level not in ["SEVERE", "ERROR"]:
                continue

            # пропускаем рекламные домены
            if any(domain in msg for domain in IGNORED_DOMAINS):
                continue

            real_errors.append(entry["message"])

    with allure.step("Проверяем, что нет реальных JS ошибок"):
        if real_errors:
            allure.attach("\n".join(real_errors), "Real_JS_errors", allure.attachment_type.TEXT)
            allure.attach(driver.get_screenshot_as_png(), "error_screenshot", allure.attachment_type.PNG)
            assert False, "Обнаружены реальные JS ошибки:\n" + "\n".join(real_errors)
        else:
            allure.attach(driver.get_screenshot_as_png(), "OK_no_js_errors", allure.attachment_type.PNG)
