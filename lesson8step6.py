from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, 'input_value')
    x  = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x) 
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")

    option2 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    option2.click()
    option2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
