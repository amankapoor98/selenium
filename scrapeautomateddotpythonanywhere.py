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
    driver.get("https://automated.pythonanywhere.com")
    return driver
def get_driver_Login():
    options=webdriver.EdgeOptions()
    options.add_argument("disable-Infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-link-features=AutomationControlled")
    driver=webdriver.Edge(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com/login")
    return driver
def writefile(text):
    """write text in file"""
    filename=f"{dt.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)
def main():
    driver=get_driver_home()
    #driver=get_driver_Login()
    time.sleep(2)
    element=(driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")).text
    writefile(element)
    #element=driver.find_element(by="id", value="id_username").send_keys("automated")
    #return element.text
    #driver.find_element(by="id", value="id_username").send_keys("automated")
    #driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    #print(driver.current_url)
    #driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    #time.sleep(2)
    #print(driver.current_url)
print(main())
