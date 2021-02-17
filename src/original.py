from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/anshul/Documents/Python_bot/chromedriver')
driver.maximize_window()
driver.get("https://www.expedia.ca/")

driver.find_element(By.XPATH,'//*[@id="location-field-destination-menu"]/div[1]/button').send_keys("Lax")

time.sleep(9)


driver.find_element(By.ID,'d1-btn').clear()
driver.find_element(By.ID,'d1-btn').send_keys("12/12/2020")

driver.find_element(By.ID,'d2-btn').clear()
driver.find_element(By.ID,'d2-btn').send_keys("12/20/2020")

driver.find_element(By.XPATH,'//*[@id="wizard-hotel-pwa-v2-1"]/div[2]/div[2]/button').click()


#explicit wait is based on the condition and  not on the time  and can be used on elements specific
time.sleep(2)
driver.close()