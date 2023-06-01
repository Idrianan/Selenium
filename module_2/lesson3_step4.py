import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    
    button = browser.find_element(By.XPATH, '//button')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    button = browser.find_element(By.XPATH, '//button')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
