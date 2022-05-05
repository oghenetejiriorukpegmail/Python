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
import pocket_option_trader


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


config=ConfigParser()
config.read('C:\\Users\\miner\\Documents\\Python\\Website_Clicker\\config.ini')
pocket_options='https://pocketoption.com/en/login'

driver=webdriver.Chrome(executable_path='C:/Python/chromedriver.exe',options=chrome_options)
driver.implicitly_wait(30)
driver.get(pocket_options)

#pocket_option_trader.enter(config['Credentials']['username'],'/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
#pocket_option_trader.enter(config['Credentials']['password'],'/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/input')
pocket_option_trader.enter('oghenetejiri_orukpe@yahoo.com','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
pocket_option_trader.enter('yqsqccgq','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/input')

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

print('Captcha Button Done!!!')
time.sleep(15)
print('Time to Login ....')

time.sleep(15)

pocket_option_trader.reset_timer()

pocket_option_trader(10,'usdchf',5)
print ('Ready to Trade!!!')