from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем оба числа
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    print("num1 =", num1, "num2 =", num2)

    # 2. Считаем сумму. Обязательно приводим к строке!
    total = str(int(num1) + int(num2))
    print("sum =", total)

    # 3. Выбираем значение в выпадающем списке
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(total)

    # 4. Нажимаем Submit
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