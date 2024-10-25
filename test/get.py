from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

service=Service(executable_path="../drivers/msedgedriver.exe")
driver=webdriver.Edge(service=service)

url="https://ecampus.pelitabangsa.ac.id/pb/"

driver.get(url)

assert "PELITA BANGSA" in driver.title

print(f"Title :{driver.title}")

driver.quit()