import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем кнопку — откроется новая вкладка
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 2. Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # 3. Решаем капчу на новой вкладке
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print("x =", x)

    y = calc(x)
    print("y =", y)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

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