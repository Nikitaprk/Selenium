import time
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.ozon.ru'
driver.get(url=url)
time.sleep(3)
driver.close()