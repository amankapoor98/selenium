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
    driver.get("https://www.hotstar.com/in/mypage")
    driver.find_element(by="xpath", value="/html/body/div[3]/div[2]/button").click()

    return driver

def get_driver_Login(driver):
    #driver.find_element(by="xpath", value="/html/body/div[1]/div[4]/div/div[2]/aside/nav/div[8]/a/button/span[1]").click()
    driver.find_element(by="xpath", value="/html/body/div[1]/div[4]/div/div[3]/div[1]/div/div[3]/div/button").click()
    phno=8607335847
    driver.find_element(by="id", value="7").send_keys(phno + Keys.RETURN)
    otp1=int(input("enter otp digit 1"))
    otp2=int(input("enter otp digit 2"))
    otp3=int(input("enter otp digit 3"))
    otp4=int(input("enter otp digit 4"))
    driver.find_element(by="id", value="1").send_keys(otp1)
    driver.find_element(by="id", value="2").send_keys(otp2)
    driver.find_element(by="id", value="3").send_keys(otp3)
    driver.find_element(by="id", value="4").send_keys(otp4+ Keys.RETURN)
    driver.find_element(by="xpath", value="/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/button/span/span").click()
    driver.find_element(by="xpath", value="/html/body/div[1]/div[4]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/div/span/img").click()
    return driver

def main():
    while True:
        driver=get_driver_home()
        get_driver_Login(driver)
    #element=(driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")).text
    #element=driver.find_element(by="id", value="id_username").send_keys("automated")
    #return element.text
    #driver.find_element(by="id", value="id_username").send_keys("automated")
    #driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    #print(driver.current_url)
    #driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    #time.sleep(2)
        print(driver.current_url)
print(main())



