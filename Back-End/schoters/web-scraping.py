from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Driver Initiation
service = Service(executable_path="C:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # Logic
    driver.get("https://beasiswa.kominfo.go.id/beasiswa/list/")
    print(driver.title)

    # Simpan output ke dalam file data.txt
    with open("./Back-End/kominfo/data.txt", "w", encoding="utf-8") as file:
        file.write(driver.page_source)

    time.sleep(20)

except Exception as e:
    print("Terjadi kesalahan:", e)

finally:
    driver.quit()
