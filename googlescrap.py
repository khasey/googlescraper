from selenium.webdriver.common.keys import Keys 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import colorama
import sys
from selenium.webdriver.chrome.service import Service
from progress.bar import Bar
from colorama import Back, Fore, Style


s=Service('./geckodriver')
driver = webdriver.Firefox(service=s)

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

def start():
    try:
        driver.get("https://www.google.com/")
        Banner()
    
    except:
        print("Problem with the custom header") 
             
        
def Search():
    try:
        
        if len(sys.argv) < 2:
            print("usage => python3 <prog name> <arg>")
        if len(sys.argv) > 2:
            print("correct way = python3 scrapgoogle.py [search element]")
            driver.quit()
        else:
            arg = sys.argv[1]
            driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(arg)
            driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
    
    except:
        print("pas de recherche")           

def Write():
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
        

def Next():
    try:
        
        i = 0
        j = 0
        while True:
            bar = Bar(Fore.RED + 'Pages =>',max=i, fill='#')
            ret = driver.find_element(By.XPATH,'//*[@id="pnnext"]')
            if ret:
                Write()
                time.sleep(2)
                ret.click()
                bar.next(j)
                j = j + 1
                i = i + 1
            else:
                break
    except:
        print(Fore.GREEN + "Scarp is over")
        #driver.quit()


start()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="L2AGLb"]').click()
time.sleep(2)
Search()
time.sleep(2)
Next()
driver.quit()
