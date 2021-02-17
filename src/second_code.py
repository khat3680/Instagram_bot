from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/anshul/Documents/Python_bot/chromedriver')
driver.maximize_window()
driver.get("https://www.expedia.ca/")

driver.implicitly_wait(5)

driver.find_element(By.XPATH, '//*[@id="uitk-tabs-button-container"]/li[2]/a').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="uitk-tabs-button-container"]/li[2]/a').send_keys("Lax")
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="location-field-leg1-origin-menu"]/div[1]/button').send_keys("Toronto, ON (YYZ-Pearson Intl.)")
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="location-field-leg1-destination-menu"]/div[1]/button').send_keys("Los Angeles, CA (LAX-Los Angeles Intl.)")
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="d1-btn"]').clear()
driver.find_element(By.XPATH,'//*[@id="d1-btn"]').send_keys("2020/12/26")

driver.find_element(By.XPATH,'//*[@id="d2-btn"]').clear()
driver.find_element(By.XPATH,'//*[@id="d2-btn"]').send_keys("2020/12/30")
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()
time.sleep(2)

#explicit wait is based on the condition and not on the time and can be used on elements specific
time.sleep(2)
driver.close()


