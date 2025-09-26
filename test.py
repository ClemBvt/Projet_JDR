from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
    driver = webdriver.Chrome()
    driver.get('http://localhost:8000/')
    return driver

def createCharacter(driver):
    driver.find_element(By.ID, "character_name").send_keys("TestCharacter")
    time.sleep(1)
    driver.find_element(By.ID, "button").click()
    time.sleep(1)

def play(driver):
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(1)

def main():
    driver = setup()
    createCharacter(driver)
    play(driver)

if __name__ == "__main__":
    main()
