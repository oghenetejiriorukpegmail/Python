import configparser
from curses.ascii import ESC
from logging import exception
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains    
from selenium.webdriver.common.keys import Keys
import time, random
from configparser import ConfigParser
import os
from telethon import TelegramClient
from telethon import events
import os, re
import time
import asyncio
import configparser
import datetime


os.chdir('C:\\Python\\Telegram')

def clicker(element_locator):
    try:
        click=driver.find_element(By.XPATH, element_locator)
        click.click()
    
    except Exception as e:
        print(e)

def enter(param,xpath):
    credential=driver.find_element(By.XPATH, xpath)
    #credential.clear()
    credential.send_keys(param)

def reset_timer():
    try:
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
    except Exception as e:
        print ('error in reset timer', e)

def set_timer(time):
    try:
        reset_timer()
        clicker('//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[2]/div[1]/div')
        for num in range (int(time)-1):
            clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[1]')
    except Exception as e:
        print ('error in set timer', e)

def check_payout():
        try:
            payout = driver.find_element(By.XPATH,'//*[@id="put-call-buttons-chart-1"]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span')
            print(currency,':',payout.text[1:-1])
            if int(payout.text[1:-1]) <= 60:
                print ('Payout too low!!!')
                return 'ignore'
        except Exception as e:
            print ('There is an issue with the check payout function', e)

def check_payout_currency(currency):
        try:
            clicker('//*[@id="bar-chart"]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/a')
            payout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal-root"]/div[2]/div/div/div[2]/div[1]/div[1]/input'))).send_keys(currency)
            payout_value = driver.find_element(By.XPATH,'//*[@id="modal-root"]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/ul/li/a/span[4]/span')
            print(currency,':',payout.text[1:-1])
            return int(payout.text[1:-1])

        except Exception as e:
            print ('There is an issue with the check payout function', e)

def compare_payouts(currency_list):
    try:
        payout_list = []
        for i in currency_list:
            payout_list.append(int(check_payout_currency(i)))
        print (max(payout_list))
        return

    except Exception as e:
        print ('There is an issue with the compare payout function', e)

def prepare(instrument):
    try:
        #Select Instrument To Trade
        clicker('//*[@id="bar-chart"]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/a/div/span')
        enter(instrument,'//*[@id="modal-root"]/div[2]/div/div/div[2]/div[1]/div[1]/input')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/ul/li/a/span[3]'))).click()
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#        set_timer(2)
    except Exception as e:
        print ('There is an issue with the prepare function', e)

def pocket_option_trader(action, duration):
    try:
        #Set Expiration
        set_timer(duration)
        #print ('Duration Set')
        #time.sleep(1)
        #Input Trade Amount
        #enter (trade_amount, '//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[2]/div[2]/div[1]/div/input')
        #Take a Trade
        if action.lower() == "buy":
            print ('Its a CALL!!!!!!!')
            a = ActionChains(driver)
            a.key_down(Keys.SHIFT).send_keys('W').perform()
#            reset_timer()
        elif action.lower() == "sell":
            print ('Its a PUT!!!!!!!')
            a = ActionChains(driver)
            a.key_down(Keys.SHIFT).send_keys('S').perform()
        return
        
    except Exception as e:
        print ('error in pocket_option_trader', e)


def profit_checker():
    profit = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/header/div[2]/div[3]/div/a/span')
    return float(profit.text)


def random_break():
    time.sleep(random.choices(30,60,90,120))

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
#chrome_options.add_argument("--headless")
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

pocket_options='https://pocketoption.com/en/login'

driver=webdriver.Chrome(executable_path='C:/Python/chromedriver.exe',options=chrome_options)
driver.implicitly_wait(30)
driver.get(pocket_options)


enter('tejiri.fai1@gmail.com','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
enter('H27VGUJQ','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/input')
#enter('oghenetejiri_orukpe@yahoo.com','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
#enter('rsBUlxEr','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/input')


WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

print('Captcha Button Done!!!')
time.sleep(15)
print('Time to Login ....')

time.sleep(5)

print('Resetting Timer...')
reset_timer()

print('Logging Into Telegram to Get Signals...')

config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']


client = TelegramClient('tradingview_robot', api_id, api_hash)
currency = ''
try:
    @client.on(events.NewMessage())
    async def my_event_handler(event):
        global currency
        currency_list =[]
        with open('results_new.csv', 'a') as f, open('results_real.csv', 'a') as r:
            if ('1676626725' in str(event.peer_id)) or ('1366707521' in str(event.peer_id)):
                event_text = event.text.strip().lower()
                print(event_text)
                event_list = event_text.split('\n')
                print(event_list)
                for n in event_list:
                    currency = n.split(':')[0]
                    print (currency)
                    action = n.split(':')[1]
                    duration = 2
                    currency_list.append(currency)
                    prepare(currency)
#                print(currency_list)
#                best_currency = compare_payouts(currency_list)
#                print("Taking the", best_currency, 'trade...')
#                prepare(best_currency)
                    if check_payout() != 'ignore':
                        pocket_option_trader(action,duration)
            
                

    client.start()
    #print('Wins:', win_count,',', 'Losses:', loss_count)
    client.run_until_disconnected()
except Exception as e:
    print (e)    