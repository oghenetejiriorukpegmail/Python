import configparser
from logging import exception
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from configparser import ConfigParser
import sys


chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
#chrome_options.add_argument("--headless")


def clicker(element_locator):
    try:
        click=driver.find_element(By.XPATH, element_locator)
        click.click()
    
    except:
        print(exception)

def login(param,xpath):
    credential=driver.find_element(By.XPATH, xpath)
    credential.send_keys(param)

config=ConfigParser()
config.read('C:\\Users\\miner\\Documents\\Python\\Website_Clicker\\config.ini')
#print(config.sections())
cryptostackers=config['Websites']['cryptostackers']
#coinstats=config['Websites']['coinstats']

driver=webdriver.Chrome(executable_path='C:/Users/miner/Documents/Python/chromedriver.exe',options=chrome_options)
driver.implicitly_wait(100)

driver.get(cryptostackers)

clicker('/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[4]/div/button')
clicker('/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[2]/div/div')

login(config['Credentials']['username'],'/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/input')
login(config['Credentials']['password'],'/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/input')

time.sleep(1)

clicker('/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div[4]/div/button')
clicker('/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/button')

time.sleep(5)

driver.close()

print('All Done!!!  Exiting...')


'''
config['Websites'] = {
    'cryptostackers':'www.cryptostackers.pro'
}
config['Actions'] = {
    'cryptostackers':'click'
}
config['Credentials'] = {
    'username':'cciephantom',
    'password':'Ideraoluwa@01'
}

f = open('config_pasrser.ini', 'w')
config.write(f)
'''
