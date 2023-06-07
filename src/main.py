# Libraries
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# config
website = r'http://www.kemx.keint.com:82/StationRates/'
driver_path = r'drivers\msedgedriver.exe'

# options from page
edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--start-maximized')
edge_options.add_argument("--remote-allow-origins=*")
edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
edge_options.add_experimental_option("prefs", {"user_experience_metrics": {"personalization_data_consent_enabled": False}})
edge_options.add_argument('--disable-extensions') 
edge_options.add_argument('--disable-infobars')
edge_options.add_argument('--disable-sync')
edge_options.add_argument('--disable-features=AccountConsistency')
time.sleep(2)

service = Service(driver_path)
driver = webdriver.Edge(service = service, options = edge_options)

# Inicializacion de navegador
driver.get(website)
WebDriverWait(driver=5).until(EC.element_to_be_clickable(By.CSS_SELECTOR))

time.sleep(2)

