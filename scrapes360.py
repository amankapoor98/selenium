from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt

driver_path = "C:\\Users\\v-amanlnu\\Downloads\\edgedriver_win64\\msedgedriver.exe"
service = EdgeService(executable_path=driver_path)

def get_driver_home():
    options=webdriver.EdgeOptions()
    options.add_argument("disable-Infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-link-features=AutomationControlled")
    driver=webdriver.Edge(service=service, options=options)
    driver.get("https://titan22.com/")
    return driver
