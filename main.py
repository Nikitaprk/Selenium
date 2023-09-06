import time
import pytest
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.vk.com'

driver.get(url=url)
time.sleep(3)
driver.close()
