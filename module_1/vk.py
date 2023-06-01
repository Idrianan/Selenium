from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = 'http://vk.com'

try:
    browser = webdriver.Chrome()
    browser.get(link)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
