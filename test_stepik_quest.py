import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN = "PolovnikovTU@yandex.ru"
PASSWORD = "qWERTY4398"

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

collected_message = []

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    # Выполняем авторизацию один раз на всю сессию тестов
    driver.get("https://stepik.org/catalog?auth=login")
    wait = WebDriverWait(driver, 15)
    try:
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "login")))
        email_input.send_keys(LOGIN)
        pass_input = driver.find_element(By.NAME, "password")
        pass_input.send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__profile-toggler, .navbar-user-card")))
        print("\nУспешная авторизация на Stepik.")
    except Exception as e:
        print(f"\nОшибка при авторизации: {e}")
        
    yield driver
    driver.quit()

@pytest.mark.parametrize('link', links)
def test_stepik_alien_message(browser, link):
    browser.get(link)
    wait = WebDriverWait(browser, 15)
    
    # Если шаг уже решался ранее, нажимаем "Решить снова"
    again_buttons = browser.find_elements(By.CSS_SELECTOR, "button.again-btn, button.attempt-wrapper-button")
    for btn in again_buttons:
        if btn.is_displayed():
            try:
                btn.click()
                time.sleep(1)
            except Exception:
                pass
    
    # Ожидаем поле ввода
    textarea = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.ember-text-area, textarea.string-quiz__textarea, textarea")))
    
    # Очищаем поле и вводим ответ
    textarea.clear()
    answer = str(math.log(int(time.time())))
    textarea.send_keys(answer)
    
    # Нажимаем кнопку "Отправить"
    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    submit_btn.click()
    
    # Дожидаемся фидбека
    hint = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint, .attempt-message_wrong, .attempt-message_correct")))
    feedback_text = hint.text.strip()
    
    # Если пришел кусочек послания (не "Correct!"), сохраняем его
    if feedback_text != "Correct!":
        print(f"\n[!] Найден кусочек послания: {feedback_text}")
        collected_message.append(feedback_text)
        assert feedback_text == "Correct!", f"Послан кусочек сообщения: {feedback_text}"
    else:
        assert feedback_text == "Correct!"

def pytest_sessionfinish(session, exitstatus):
    if collected_message:
        print("\n\n" + "="*50)
        print("СОБРАННОЕ ПОСЛАНИЕ ИНОПЛАНЕТЯН:")
        print(" ".join(collected_message))
        print("="*50 + "\n")
