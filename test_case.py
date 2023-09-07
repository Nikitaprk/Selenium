import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://localhost/litecart/admin/login.php")  # переход на страницу
driver.find_element(By.NAME, 'username').send_keys('login')  # поиск поля логин, отправка значений
driver.find_element(By.NAME, 'password').send_keys('password')  # поиск поля пароля, отправка значений
driver.find_element(By.NAME, 'remember_me').click()  # поиск чекбокса, клик
time.sleep(3)
driver.find_element(By.NAME, 'login').click()  # поиск кнопки "логин", клик
driver.close()