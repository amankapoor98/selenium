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
def get_driver_Register(driver):
    driver.find_element(by="xpath", value="/html/body/header/div[1]/div[1]/div/div[3]/a[2]").click()
    driver.find_element(by="xpath", value="/html/body/main/article/section/div/div[1]/form/div[3]/a[1]").click()
    driver.find_element(by="id", value="customer[accepts_terms]").click()
    driver.find_element(by="id", value="FirstName").send_keys("Aman")
    driver.find_element(by="id", value="LastName").send_keys("Kapoor")
    driver.find_element(by="id", value="Email").send_keys("mramankapoor@hotmail.com")
    driver.find_element(by="id", value="CreatePassword").send_keys("Aa@8607335847")
    driver.find_element(By.CSS_SELECTOR, ".button.button.button--primary").click()
    time.sleep(10)
    return driver
def get_driver_Login(driver):
    driver.find_element(by="xpath", value="/html/body/header/div[1]/div[1]/div/div[3]/a[2]").click()
    driver.find_element(by="id", value="CustomerEmail").send_keys("amankapoor8274@gmail.com")
    driver.find_element(by="id", value="CustomerPassword").send_keys("Aa@8607335847" + Keys.RETURN)
    #driver.find_element(By.CSS_SELECTOR, ".button.button.button--primary").click()
    #driver.find_element(By.CSS_SELECTOR, ".button-submit.button").click()
    time.sleep(10)
    return driver
def main():
    driver=get_driver_home()
    #driver=get_driver_Register(driver)
    driver=get_driver_Login(driver)
    #element=(driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")).text
    #element=driver.find_element(by="id", value="id_username").send_keys("automated")
    #return element.text
    #driver.find_element(by="id", value="id_username").send_keys("automated")
    #driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    #print(driver.current_url)
    #driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)
    time.sleep(10)
print(main())
