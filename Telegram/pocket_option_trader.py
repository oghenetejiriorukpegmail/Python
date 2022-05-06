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
    
    except:
        print(exception)

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
    except:
        print ('error in reset timer')

def set_timer(time):
    try:
        for num in range (int(time)-1):
            clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[1]')
    except:
        print ('error in set timer')

def pocket_option_trader(instrument,duration):
    try:
        #Set Expiration
        reset_timer()
        set_timer(duration)

        time.sleep(1)
        print('Timer Reset Completed')
        #Select Instrument To Trade
        clicker('//*[@id="bar-chart"]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/a/div/span')
        enter(instrument,'//*[@id="modal-root"]/div[2]/div/div/div[2]/div[1]/div[1]/input')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/ul/li/a/span[3]'))).click()
        payout = driver.find_element(By.XPATH,'//*[@id="put-call-buttons-chart-1"]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span')
        print(instrument,':',payout.text)
        if int(payout.text[1:-2]) >= 50:
            print ('Payout too low!!!')

        time.sleep(1)
#        clicker('//*[@id="bar-chart"]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/a/div/span')
        #Input Trade Amount
        #enter (trade_amount, '//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[2]/div[2]/div[1]/div/input')

    #    time.sleep(1)
    #    #Take a Trade
    #    if action.lower() == "buy":
    #        print ('Its a CALL!!!!!!!')
    #        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, long))).click()
    #    elif action.lower() == "sell":
    #        print ('Its a PUT!!!!!!!')
    #       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, short))).click()
        return
        
    except:
        print ('error in pocket_option_trader')


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


enter('oghenetejiri_orukpe@yahoo.com','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
enter('yqsqccgq','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/input')

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


client = TelegramClient('binarex_robot', api_id, api_hash)
currency = ''
@client.on(events.NewMessage())
async def my_event_handler(event):
    with open('results_new.csv', 'a') as f:
#        if "1518994770" in str(event.peer_id):
        if "1366707521" in str(event.peer_id):
    #        print (event.text)
            event_list = event.text.strip().lower().split()
            print(event_list)
    #        print('prepare' in event.text.lower(),'prepare')
    #        print('signal' in event.text.lower(),'signal')
    #        print('summary' in event.text.lower(),'summary')
            if 'prepare' in event.text.lower():
                print(datetime.datetime.now(), ':', "Curency: ",str(event_list[3])[2:6]+str(event_list[3])[8:])
                f.write(str(datetime.datetime.now())+': '+str(event_list[3])[2:6]+str(event_list[3])[8:]+', ')
                currency = str(event_list[3])[2:6]+str(event_list[3])[8:]
                with open('currency.txt', 'w') as c:
                    c.write(currency)                    
            elif 'signal' in event.text.lower():
                with open('currency.txt', 'r') as c:
                    currency = c.read()
                print (currency)
    #           print ('signal in event.text')
                if 'safe' in event.text.lower():
    #               print ('safe in event.text')
                    print('Action:', re.sub(r'[()]','',str(event_list[4])).upper()+',', "Duration:", event_list[12])
                    f.write('0, ')
                    pocket_option_trader(currency,event_list[12])
                else:
                    print('Action:', re.sub(r'[()]','',str(event_list[2])).upper()+',', "Duration:", event_list[5])
                    pocket_option_trader(currency,event_list[5])
            elif 'summary' in event.text.lower():
    #            print('summary in the list')
                if 'safe' in event.text.lower():
    #                print('summary and safe  in event.text')
                    print('Result:', str(event_list[4])[2:6]+str(event_list[4])[8:]+',', str(event_list[-1])[:-1])
                    if str(event_list[-1])[:-1].lower() == 'profit':
                        f.write('1\n')
                    elif str(event_list[-1])[:-1].lower() == 'loss':
                        f.write('0\n')
                else:
                    if str(event_list[-1])[:-1].lower() == 'profit':
                        f.write('1\n')
                    elif str(event_list[-1])[:-1].lower() == 'loss':
                        f.write('0\n')
                    else:
                        f.write(' \n')
                    print('Result:', str(event_list[1])[2:6]+str(event_list[1])[8:]+',', str(event_list[-1])[:-1])
               

client.start()
#print('Wins:', win_count,',', 'Losses:', loss_count)
client.run_until_disconnected()