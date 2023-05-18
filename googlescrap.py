from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver.common.by import By
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

driver = webdriver.Firefox(service=Service('./geckodriver'))
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

