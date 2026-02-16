from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class ElPaisScraper:
    def __init__(self):
        self.base_url = "https://elpais.com"
        self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub")


    #func to open opinion
    def open_opinions_section(self):
        self.driver.get("https://elpais.com/opinion/")
        
        wait = WebDriverWait(self.driver, 10)

        try:
            constent_button=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Aceptar')]")))
            constent_button.click()
        except:
            pass


    #func to get 1st five artiles
    def get_first_five_article_links(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article h2 a")))

        article_elements = self.driver.find_elements(By.CSS_SELECTOR, "article h2 a")

        links = []
        for element in article_elements[:5]:
            link = element.get_attribute("href")

            if link and link.startswith("https://elpais.com/opinion/") and link.endswith(".html"):
                if link not in links:
                    links.append(link)
            
            if len(links) == 5:
                break

        return links
    

    #func to exract article details
    def extract_article_details(self, link):
        self.driver.get(link)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        title = self.driver.find_element(By.TAG_NAME, "h1").text
        time.sleep(2)

        # Get full page source
        html = self.driver.page_source

        soup = BeautifulSoup(html, "html.parser")

        article_tag = soup.find("article")

        content = ""

        if article_tag:
            paragraphs = article_tag.find_all("p")

            content_list = []
            for p in paragraphs:
                text = p.get_text().strip()
                if len(text) > 40:
                    content_list.append(text)

            content = "\n".join(content_list)

        #image extraction
        image_url = None
        try:
            img = self.driver.find_element(By.CSS_SELECTOR, "article img")
            image_url = img.get_attribute("src")
        except:
            print("No image found.")

        return title, content, image_url


    #func to download imagess
    def download_image_from_url(self, img_url, index):
        try:
            img_data = requests.get(img_url).content

            if not os.path.exists("images"):
                os.makedirs("images")

            with open(f"images/article_{index}.jpg", "wb") as handler:
                handler.write(img_data)

        except:
            print("Failed to download image.")
