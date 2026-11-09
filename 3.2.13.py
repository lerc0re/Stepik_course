import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        # Заполняем поля
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("test@test.com")
        
        # Нажимаем кнопку
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        
        # Проверяем результат
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Ошибка при регистрации")
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        # Заполняем поля
        # На этой странице разработчики допустили баг (поле пропало), 
        # поэтому здесь выбросится NoSuchElementException, и тест упадёт
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("test@test.com")
        
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Ошибка при регистрации")
        browser.quit()

if __name__ == "__main__":
    unittest.main()