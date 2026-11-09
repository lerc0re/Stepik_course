from selenium import webdriver
from selenium.webdriver.common.by import By

def test_registration1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("test@test.com")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!", "Ошибка при регистрации"
    browser.quit()

def test_registration2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Здесь упадет из-за бага на странице
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("test@test.com")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!", "Ошибка при регистрации"
    browser.quit()