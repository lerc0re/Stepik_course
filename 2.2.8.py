import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("test@test.com")

    # Формируем путь к файлу, который лежит рядом со скриптом
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "bio.txt")

    # Загружаем файл
    browser.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(file_path)

    # Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Забираем код из alert
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

    time.sleep(10)

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла