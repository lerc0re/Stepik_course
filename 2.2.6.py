import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print("x =", x)

    # 2. Считаем функцию
    y = calc(x)
    print("y =", y)

    # 3. Скроллим страницу вниз — освобождаем элементы от футера
    browser.execute_script("window.scrollBy(0, 100);")

    # 4. Вводим ответ в текстовое поле
    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)

    # 5. Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    # 6. Выбираем radiobutton "Robots rule!"
    robots_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_radio.click()

    # 7. Нажимаем Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Забираем код из alert
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

    time.sleep(10)

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла