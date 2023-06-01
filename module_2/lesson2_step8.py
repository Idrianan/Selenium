import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_element = browser.find_element(By.NAME,'firstname')
    first_name_element.send_keys('ARTEM')

    second_name_element = browser.find_element(By.NAME,'lastname')
    second_name_element.send_keys('PLATONOV')

    email_element = browser.find_element(By.NAME,'email')
    email_element.send_keys('idrianchanel@gmail.com')

    file_element = browser.find_element(By.ID,'file')
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt')
    file_element.send_keys(file_path)

    btn = browser.find_element(By.TAG_NAME,'button')
    btn.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
