#Module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


#Driver Initiation
service = Service(executable_path="C:\chromedriver.exe")
driver =webdriver.Chrome(service=service)


#Logic
driver.get("https://beasiswa.kominfo.go.id/beasiswa/list/")
print(driver.title)

search = driver.find_elements
print(driver.page_source)

time.sleep(20)

driver.quit()