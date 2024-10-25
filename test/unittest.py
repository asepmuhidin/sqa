import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path="../drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://ecampus.pelitabangsa.ac.id/pb/login")

input_username = driver.find_element(By.NAME, "j_username")
input_password = driver.find_element(By.NAME, "j_password")

input_username.clear()
input_password.clear()

input_username.send_keys("admin")
input_password.send_keys("admin")

link = driver.find_element(By.CLASS_NAME, "btnlogin")
link.click()
time.sleep(10)
driver.close()