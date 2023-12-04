from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


Selenium_Service = Service(ChromeDriverManager().install())
Navigator = webdriver.Chrome()

Navigator.get('http://localhost:5000')

print(Navigator.title)
time.sleep(5)
