from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ссылка на СТАРУЮ (правильную) версию страницы
link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поля формы
    # Поле First name — ищем по placeholder
    first_name = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    first_name.send_keys("Ivan")

    # Поле Last name — ищем по placeholder
    last_name = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    last_name.send_keys("Petrov")

    # Поле Email — ищем по placeholder
    email = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your email']")
    email.send_keys("test@test.com")

    # Кнопка Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждём загрузки страницы с результатом
    time.sleep(1)

    # Проверяем, что регистрация прошла успешно
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # Проверяем текст (это уже часть теста)
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла