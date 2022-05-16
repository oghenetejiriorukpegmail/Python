import configparser
from curses.ascii import ESC
from locale import currency
from logging import exception
from pickle import FALSE
from tkinter import E
from tkinter.messagebox import NO
from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
    
    except:
        print(exception)

def enter(param,xpath):
    credential=driver.find_element(By.XPATH, xpath)
    #credential.clear()
    credential.send_keys(param)

def reset_timer():
    try:
        check_timer = driver.find_element(By.XPATH,'//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[1]')
#        print(check_timer.text)
        if 'utc' in str(check_timer.text).lower():
            #change to fixed duration
            clicker('//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[2]/div[2]/div/a')
        clicker('//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[2]/div[1]/div')
        #Reset to 1min
#       #Reset  Minutes
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/div/input'))).click()
        ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(1).perform()
#        enter(1,'//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/div/input')
#       #Reset  Hours
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[1]/div[1]/div/input'))).click()
        ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(0).perform()
#        enter(0, '//*[@id="modal-root"]/div[2]/div/div/div[1]/div[1]/div/input')
#       #Reset Seconds
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[1]/div[3]/div/input'))).click()
        ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(0).perform()
#        enter(0,'//*[@id="modal-root"]/div[2]/div/div/div[1]/div[3]/div/input')


#            #reset the hour
#            clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[1]/a[2]')
#        for i in range (10):
#            #reset the minutes
#            clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/a[2]')
#        for i in range (10):
#            #reset the seconds
#            clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div[3]/a[2]')
    except:
        print ('error in reset timer')

def set_minute_timer(time, otc):
    try:
        #reset_timer()
        if otc == True:
            clicker ('//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[2]/div[1]/div')
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/div/input'))).click()
            ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(time).perform()
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[1]/div[3]/div/input'))).click()
            ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(0).perform()
        clicker ('//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[1]/div[2]/div[1]/div')
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[1]/div[2]/div/input'))).click()
        ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(time).perform()
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[1]/div[3]/div/input'))).click()
        ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(0).perform()   
        clicker('//*[@id="chart-1"]/canvas')    
        
    except Exception as e:
        print ('error in set minute timer', e)

def check_payout():
    global payout_path, payout_threshold, ignore
    try:
#            payout_value_path = '//*[@id="put-call-buttons-chart-1"]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span'
        payout = driver.find_element(By.XPATH, payout_path)
        print(currency,':',payout.text[1:-1])
        if int(payout.text[1:-1]) < payout_threshold:
#            print ('Payout too low!!!')
            ignore = True
        else:
            ignore = False
    except Exception as e:
        print ('There is an issue with the check payout function', e)

def prepare(instrument):
    global ignore 
    market_check()
    if ignore == False:
        try:
            #Select Instrument To Trade
            clicker('//*[@id="bar-chart"]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/a/div/span')
            clicker('//*[@id="modal-root"]/div[2]/div/div/div[1]/div/div[1]/a[1]/span[2]')
            enter(instrument,'//*[@id="modal-root"]/div[2]/div/div/div[2]/div[1]/div[1]/input')
            try:
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/ul/li/a/span[3]'))).click()
            except:
                ignore = True
                print ('Ignoring due to instrument unavailability')
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            reset_timer()
        except:
            print ('There is an issue with the prepare function')

def pocket_option_trader(action, duration, otc):
    try:
        #Set Expiration
        set_minute_timer(duration, otc)
        #print ('Duration Set')
        #time.sleep(1)
        #Input Trade Amount
        trade_amount = 10
    #    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="put-call-buttons-chart-1"]/div/div[1]/div[2]/div[2]/div[1]/div/input'))).click()
    #    ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys('10').perform()
        #Take a Trade
        check_payout()
        if ignore == False:
            if action.lower() == 'buy':
                ActionChains(driver).key_down(Keys.SHIFT).send_keys('W').key_up(Keys.SHIFT).perform()
                print ('Its a CALL!!!!!!!')
            elif action.lower() == 'sell':
                ActionChains(driver).key_down(Keys.SHIFT).send_keys('S').key_up(Keys.SHIFT).perform()
                print ('Its a PUT!!!!!!!')
            return
        else:
            print('Payout Too Low') 
        
    except Exception as e:
        print ('error in pocket_option_trader', e)

def profit_checker():
    global otc
#    if otc == True:
#        profit = driver.find_element(By.XPATH,'//*[@id="put-call-buttons-chart-1"]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span')
    profit = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/header/div[2]/div[2]/div/a/span')
    return float(profit.text)

def compare_payouts(currency_list):
    payout_list = []
    for i in currency_list:
        payout_list.append(check_payout(i))


def random_break():
    choices = [30*60,60*60,90*60,120*60]
    choice = random.choice(choices)
    print ('Break Time:', choice)
    time.sleep(choice)

def market_check():
    global otc, ignore
    market = driver.find_element(By.XPATH,'//*[@id="bar-chart"]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/a/div/span')
    print (market.text)
    if 'otc' in market.text:
        if otc == True:
            ignore = False
        else:
            ignore = True
            print('Market Mismatch!!!')
    else:
        if otc == True:
            ignore = True
            print('Market Mismatch!!!')
        else:
            ignore = False

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
driver.implicitly_wait(5)
driver.get(pocket_options)


#enter('tejiri.fai1@gmail.com','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
#enter('H27VGUJQ','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/input')
enter('cciephantom@gmail.com','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
enter('Ideraoluwa@01','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/input')
#enter('oghenetejiri_orukpe@yahoo.com','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
#enter('rsBUlxEr','/html/body/div[2]/div[2]/div/div/div/div[3]/form/div[2]/div[2]/input')

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

print('Captcha Button Done!!!')
time.sleep(15)
print('Time to Login ....')
reset_timer()
time.sleep(5)

print('Logging Into Telegram to Get Signals...')

config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

payout_path = '//*[@id="put-call-buttons-chart-1"]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span'
payout_threshold = 74
ignore = False
cool_off = 0
cool_off_trigger = 10
currency = ''
otc = True
action = ''
duration = 0
safe = True

initial_balance = profit_checker()
print (initial_balance)
target_balance = float(input('Target for this session:'))

client = TelegramClient('binarex_robot', api_id, api_hash)
@client.on(events.NewMessage())
async def my_event_handler(event):
    global ignore, cool_off, otc, currency, action, duration, safe
    with open('results_new.csv', 'a') as f, open('results_real.csv', 'a') as r:
        if ('1518994770' in str(event.peer_id)) or ('1366707521' in str(event.peer_id)):
#        if "1366707521" in str(event.peer_id):
    #        print (event.text)
            event_list = event.text.strip().lower().split()
            print(event_list)
            if 'prepare' in event.text.lower():
                print(datetime.datetime.now(), ':', "Curency: ",str(event_list[3])[2:6]+str(event_list[3])[8:], 'Balance: ', profit_checker())
                f.write(str(datetime.datetime.now())+': '+str(event_list[3])[2:6]+str(event_list[3])[8:]+', ')
                currency = str(event_list[3])[2:5]+str(event_list[3])[8:]
                if 'otc' in event.text.lower():
                    otc = True
                prepare(currency)
                with open('currency.txt', 'w') as c:
                    c.write(str(profit_checker()))  
                r.write(currency+', ')                  
            elif ('completed' in event.text.lower()) or ('finished' in event.text.lower()):
                time.sleep(5)
                with open('currency.txt', 'r') as c:
                    old_balance = float(c.read())
                new_balance = profit_checker()
                if new_balance > old_balance:
                    print (new_balance, 'Profit')
                    r.write('1\n')
                    cool_off = 0
                elif new_balance < old_balance:
                    print (new_balance, 'Loss')
                    r.write('0\n')
                    cool_off = cool_off + 1
                    if safe == True:
                        duration = 2
                        pocket_option_trader(action, duration, otc)
                        time.sleep(duration)
                else:
                    print ('Draw')
                    r.write('\n')
                if new_balance >= 1.1*initial_balance:
                    client.disconnect()
                elif new_balance >= target_balance:
                    await client.disconnect()
                ignore = False
                if cool_off == cool_off_trigger:
                    print('Two Losses in a Roll, Cooling off for some random time')
                    cool_off = 0
                    random_break()

            elif 'signal' in event.text.lower():
                print ('Ignore:', ignore)
                action =  re.sub(r'[()]','',str(event_list[2])).upper()
                duration = int(event_list[5])
                print('Action:', action,'Currency:', currency, 'Duration:', duration)
                if ignore == False:
                    pocket_option_trader(action, duration, otc)

               

client.start()
#print('Wins:', win_count,',', 'Losses:', loss_count)
client.run_until_disconnected()