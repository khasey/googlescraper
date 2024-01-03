import random
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from progress.bar import Bar
from colorama import Fore, Style
import colorama

# Constantes et paramètres
BING_URL = "https://www.bing.com/?cc=fr"
SEARCH_BOX_XPATH = '//*[@id="sb_form_q"]'
NEXT_BUTTON_CSS = '.sb_pagN'
CAPTCHA_XPATH = '//*[@id="bnp_container"]'
CAPTCHA_REFUSE_XPATH = '//*[@id="bnp_btn_reject"]'

USER_AGENTS = [
   'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',  # Tor Browser for Windows and Linux
    'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0',  # Tor Browser for Android
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '

    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
]

class BingScraper:
    def __init__(self):
        self.driver = self.init_driver()

    def init_driver(self):
        options = FirefoxOptions()
        options.add_argument('--headless')
        options.log.level = "trace"
        options.add_argument(f'user-agent={random.choice(USER_AGENTS)}')
        driverService = Service('./geckodriver')
        return webdriver.Firefox(service=driverService, options=options)

    def start(self, query):
        self.navigate_to_bing()
        self.handle_captcha()
        # time.sleep(2)
        self.search(query)
        # time.sleep(2)
        self.scrape_results()

    def navigate_to_bing(self):
        self.driver.get(BING_URL)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "sb_form_q")))

    def handle_captcha(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, CAPTCHA_XPATH)))
            refuse_button = self.driver.find_element(By.XPATH, CAPTCHA_REFUSE_XPATH)
            refuse_button.click()
        except:
            pass  # Pas de captcha détecté

    def search(self, query):
        search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, SEARCH_BOX_XPATH)))
        search_box.send_keys(query)
        # search_box.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search_icon > svg:nth-child(1)"))).click()

    def scrape_results(self):
        count = 0 # Vous pouvez ajuster le max si nécessaire
        while True:
            bar = Bar(Fore.GREEN + 'Pages =>'+ Fore.CYAN, max=200, fill='#')
            try:
                next_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, NEXT_BUTTON_CSS)))
                self.write_results()
                next_link.click()
                bar.next(count)
                count += 1
            except:
                break
        bar.finish()

    def write_results(self):
        cites = self.driver.find_elements(By.TAG_NAME, 'cite')
        with open('websitegoogle.txt', 'a') as f:
            for cite in cites:
                if cite.text.startswith("http"):
                    f.write("%s\n" % cite.text)

def main():
    if len(sys.argv) < 2:
        print("usage => python3 <prog name> <args>")
        return

    colorama.init(autoreset=True)
    print_banner()

    scraper = BingScraper()
    for query in sys.argv[1:]:
        print(f"Processing argument: {query}")
        scraper.start(query)

    scraper.driver.quit()

def print_banner():
    print(Fore.RED + """
  ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███  
▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒
░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒
  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒
    ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░
    ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░
    ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░     
   ░  ░  ░  ░          ░░   ░   ░   ▒   ░░       
    ░  ░ ░         ░           ░  ░         
        ░    Best Scrap Engine made by @Khasey                               
          """)

if __name__ == "__main__":
    main()
