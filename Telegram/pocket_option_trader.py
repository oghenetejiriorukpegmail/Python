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

os.chdir('C:\\Python\\Telegram')

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
    credential.clear()
    credential.send_keys(param)

def reset_timer():
    check_timer = driver.find_element(By.XPATH,'//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[1]')
#    print(check_timer.text)
    if 'utc' in str(check_timer.text).lower():
        #change to fixed duration
        clicker('//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[2]/div[2]/div/a')
    clicker('//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[2]/div[1]/div')
    for i in range (10):
        #reset the hour
        clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[1]/a[2]')
    for i in range (10):
        #reset the minutes
        clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[2]')
    for i in range (10):
        #reset the seconds
        clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[3]/a[2]')


def set_timer(time):
    for num in range (time-1):
        clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[1]')

def pocket_option_trader(trade_amount,instrument,duration,action):
    #Set Expiration
    reset_timer()
    set_timer(duration)

    time.sleep(1)

    #Select Instrument To Trade
    clicker('//*[@id="bar-chart"]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/a/div/span')
    login(instrument,'//*[@id="modal-root"]/div[2]/div/div/div[2]/div[1]/div[1]/input')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/ul/li/a/span[3]'))).click()

    time.sleep(1)

    #Input Trade Amount
    login (trade_amount, '//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[2]/div[2]/div[1]/div/input')
    
    time.sleep(1)
    clicker('//*[@id="chart-1"]/canvas')
    time.sleep(1)
    #Take a Trade
    if action.lower() == "buy":
        print ('Its a CALL!!!!!!!')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, long))).click()
    elif action.lower() == "sell":
        print ('Its a PUT!!!!!!!')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, short))).click()



config=ConfigParser()
config.read('C:\\Users\\miner\\Documents\\Python\\Website_Clicker\\config.ini')
pocket_options='https://pocketoption.com/en/login'
long = '//*[@id="put-call-buttons-chart-1"]/div/div[2]/div[2]/a/span/span/span'
short = '//*[@id="put-call-buttons-chart-1"]/div/div[2]/div[3]/a/span/span/span'

driver=webdriver.Chrome(executable_path='C:/Python/chromedriver.exe',options=chrome_options)
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

time.sleep(2)

clicker('/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[4]/button')

print('Time to Login ....')
time.sleep(15)
#Set Timer
reset_timer()



pocket_option_trader(10,'usdchf',5,'buy')
time.sleep(1000)
driver.close()
