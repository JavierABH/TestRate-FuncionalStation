from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Scraper:
    def __init__(self):
        options = Options()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def start(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'example-class')))

    def get_data(self):
        data = []
        elements = self.driver.find_elements(By.XPATH, '//div[@class="example-element"]')
        for element in elements:
            data.append(element.text)

        return data

    def close(self):
        self.driver.quit()
