import configparser
from logging import exception
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from configparser import ConfigParser


def clicker(element_locator):
    try:
        click=driver.find_element_by_xpath(element_locator)
        click.click()
    
    except:
        print(exception)

def login(param,xpath):
    credential=driver.find_element(By.XPATH, xpath)
    credential.send_keys(param)

config=ConfigParser()
config.read('Website Clicker/config.ini')
#print(config.sections())
cryptostackers=config['Websites']['cryptostackers']
coinstats=config['Websites']['coinstats']

driver=webdriver.Chrome()
driver.implicitly_wait(100)
driver.get(coinstats)

clicker('//*[@id="__next"]/main/header/div/div[2]/div[3]/a[1]')
login(config['Credentials']['username'],'//*[@id="__next"]/main/div[2]/div/form/div[1]/div[1]/div/input')
login(config['Credentials']['password'],'//*[@id="__next"]/main/div[2]/div/form/div[1]/div[2]/div/input')
time.sleep(1)
clicker('//*[@id="__next"]/main/div[2]/div/form/div[2]/button')
time.sleep(5)

driver.close()

time.sleep(10)
driver.get(cryptostackers)

clicker('/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[4]/div/button')
clicker('/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[2]/div/div')

login(config['Credentials']['username'],'/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/input')
login(config['Credentials']['password'],'/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/input')

time.sleep(1)

clicker('/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div[4]/div/button')
clicker('//*[@id="confetti"]')

time.sleep(10)

driver.close()






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
