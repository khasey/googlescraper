import random
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import colorama
import sys
from selenium.webdriver.chrome.service import Service
from progress.bar import Bar
from colorama import Back, Fore, Style

def Banner():
    colorama.init(autoreset=True)
    print(Fore.RED + """                                                                      
 @@@@@@    @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@   
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
!@@       !@@       @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!       !@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!!@@!!    !@!       @!@!!@!   @!@!@!@!  @!@@!@!   @!!!:!    @!@!!@!   
 !!@!!!   !!!       !!@!@!    !!!@!!!!  !!@!!!    !!!!!:    !!@!@!    
     !:!  :!!       !!: :!!   !!:  !!!  !!:       !!:       !!: :!!   
    !:!   :!:       :!:  !:!  :!:  !:!  :!:       :!:       :!:  !:!  
:::: ::    ::: :::  ::   :::  ::   :::   ::        :: ::::  ::   :::  
:: : :     :: :: :   :   : :   :   : :   :        : :: ::    :   : :  
                                                     coded by KHASEY               
        """)

def Start(driver):
    try: driver.get("https://www.google.com/")
    except: print("Problem with the custom header")  

def Wait():
    time.sleep(5)
        
def Search(driver, current):
    try:
        driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys(current)
        driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys(Keys.ENTER)
    except:
        print("pas de recherche")           

def Write(driver):
    try:
        lnks = driver.find_elements(By.TAG_NAME,'a')
        array = []
        for i in lnks:
            if i.get_attribute('href') and 'https://www.google.com' not in i.get_attribute('href'):
                if i.get_attribute('href') not in array:
                    array.append(i.get_attribute('href'))
        with open('websitegoogle.txt', 'a') as f:
            for item in array:
                f.write("%s\n" % item)        
    except:
        print("pas de file")                    
        

def Next(driver):
    try:
        count = 0
        while True:
            bar = Bar(Fore.RED + 'Pages =>', max=count, fill='#')
            ret = driver.find_element(By.XPATH,'//*[@id="pnnext"]')
            if ret:
                Write(driver)
                time.sleep(4)
                ret.click()
                bar.next(count)
                count += 1
            else: break
    except:
        print(Fore.GREEN + "Scarp is over")

Banner()

if len(sys.argv) < 2:
    print("usage => python3 <prog name> <args>")
    exit()

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',  # Tor Browser for Windows and Linux
    'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0',  # Tor Browser for Android
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    'AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
]

options = FirefoxOptions()
options.add_argument(f'user-agent={random.choice(user_agents)}')

driver = webdriver.Firefox(service=Service('./geckodriver'), options=options)
first = True
for current in sys.argv[1:]:
    print("Processing argument: " + current)
    Start(driver)
    Wait()
    if (first):
        driver.find_element(By.XPATH, '//*[@id="L2AGLb"]').click()
        first = False
    Wait()
    Search(driver, current)
    Wait()
    Next(driver)
driver.quit()

