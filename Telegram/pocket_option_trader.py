import configparser
from logging import exception
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from configparser import ConfigParser
import os

os.chdir('C:\\Users\\miner\\Documents\\Python\\Telegram')

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
#chrome_options.add_argument("--headless")
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)


def clicker(element_locator):
    try:
        click=driver.find_element(By.XPATH, element_locator)
        click.click()
    
    except:
        print(exception)

def login(param,xpath):
    credential=driver.find_element(By.XPATH, xpath)
    credential.send_keys(param)

def reset_timer():
    check_timer = driver.find_element(By.XPATH,'//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[1]')
    print(check_timer.text)
    if 'utc' in str(check_timer.text).lower():
        clicker('//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[2]/div[2]/div/a')
    clicker('//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[2]/div[1]/div')
    
    clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[1]/a[2]')
    clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[1]/a[2]')
    clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[1]/a[2]')
    clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[1]/a[2]')
    clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[1]/a[2]')

    clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[2]')
    clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[2]')
    clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[2]')
    clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[2]')
    clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[2]')

def set_timer(time):
    for num in range (time-1):
        clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[1]')

config=ConfigParser()
config.read('C:\\Users\\miner\\Documents\\Python\\Website_Clicker\\config.ini')
pocket_options='https://pocketoption.com/en/login'


driver=webdriver.Chrome(executable_path='C:/Users/miner/Documents/Python/chromedriver.exe',options=chrome_options)
driver.implicitly_wait(1000)

driver.get(pocket_options)

#clicker('/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[4]/div/button')


#login(config['Credentials']['username'],'/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
#login(config['Credentials']['password'],'/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/input')
login('oghenetejiri_orukpe@yahoo.com','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
login('yqsqccgq','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/input')

time.sleep(1)

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

print('Captcha Button Done!!!')

#time.sleep(1)

clicker('/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[4]/button')

print('Time to Login ....')
time.sleep(10)
#Set Timer
reset_timer()

time.sleep(5)
#3mins
reset_timer()
set_timer(3)

time.sleep(10)
#5mins
reset_timer()
set_timer(3)

time.sleep(10)
#2mins
reset_timer()
set_timer(3)

time.sleep(10)

#Select Instrument To Trade
clicker('//*[@id="bar-chart"]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/a/div/span')
login('usdjpy','//*[@id="modal-root"]/div[2]/div/div/div[2]/div[1]/div[1]/input')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/ul/li/a/span[3]'))).click()

time.sleep(10)


time.sleep(1000)
driver.close()
