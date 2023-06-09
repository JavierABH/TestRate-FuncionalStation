# Libraries
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# config
website = 'http://www.kemx.keint.com:82/StationRates/'
driver_path = r'drivers\msedgedriver.exe'

def main():
    # options from page
    service = Service(driver_path)
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument('--start-maximized')
    edge_options.add_argument("--remote-allow-origins=*")
    edge_options.add_argument('--disable-extensions')
    edge_options.add_argument('--disable-infobars')
    edge_options.add_argument('--disable-sync')
    edge_options.add_argument('--disable-features=AccountConsistency')
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
    edge_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2})
    edge_options.add_experimental_option("prefs", {
        "user_experience_metrics": {"personalization_data_consent_enabled": False}})

    time.sleep(5)

    driver = webdriver.Edge(service = service, options = edge_options)

    # Inicializacion de navegador
    driver.get(website)
    time.sleep(2)
    clickable_element  = driver.find_element(By.XPATH, '//*[@id="ext-gen34"]')
    clickable_element.click()
    
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()