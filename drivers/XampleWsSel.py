from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()
#driver.get("https://code.visualstudio.com/docs/languages/python")
driver.get("http://www.kemx.keint.com:82/stationrates/")

time.sleep(3)
#driver.find_element(By.CSS_SELECTOR, '#ext-gen38').click()
txt1 = driver.find_element(By.CSS_SELECTOR, '#ext-comp-1002')
txt1.send_keys('ZF EB100')


#element = driver.find_element(By.CSS_SELECTOR, '#ext-gen37').click()
# then we can get the element text
#print(element.text)
"Availing himself of the mild, summer-cool weather that now reigned in these latitudes..."
# we can also get tag name and attributes:


#print(element.tag_name)
#print(element.get_attribute("class"))

# for multiple elements we need to iterate
#for element in driver.find_elements(By.CSS_SELECTOR, 'p'):
#    print(element.text)

time.sleep(5)
#driver.close()