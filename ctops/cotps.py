from cgi import print_exception
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

password_text='Ideraoluwa@01'

while True:
    driver=webdriver.Chrome(executable_path='C:/Users/miner/Documents/Python/chromedriver.exe')
    driver.get('https://cotps.com/#/pages/login/login?originSource=userCenter')
    driver.maximize_window()
    driver.implicitly_wait(100)
    
    username=driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-input/div/input')
    username.send_keys('6135588198')
    password=driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-input/div/input')
    password.click()
    password.clear()
    password.send_keys(password_text)
    
    time.sleep(2)

    login=driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-button')
    login.click()

    transactionHall=driver.find_element(By.XPATH, '/html/body/uni-app/uni-tabbar/div[1]/div[3]/div/div[2]')
    transactionHall.click()

    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[1]/uni-view[2]')))

    valid=False
    while not valid:
        try:
            precheck=driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[1]/uni-view[2]')
            print('In Transaction:', precheck.text)

            wallet_balance=driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]')
            print('Wallet Balance:', wallet_balance.text)
            (float(precheck.text))
        except ValueError:
            pass
            

    #f = open("cotps_session.txt", "a")
    #f.write(precheck.text)
    #f.close()

    if float(precheck.text) == 0:
        while float(wallet_balance.text) > 5:

            check_for_order=driver.find_element(By.CSS_SELECTOR, 'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view.grab-orders-wrap.grab-orders-wrap1 > uni-button')
            check_for_order.click()

            sell_order=driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]')
            sell_order.click()

            confirm_sale=driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button')
            confirm_sale.click()

            time.sleep(10)

            wallet_balance=driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button')
            print ('New Wallet Balance is:',wallet_balance.text)


        print(datetime.now(),'Session Completed!')
        session_file = open("cotps_session.txt", "a")
        log_session_to_file='Session Completed! at '+str(datetime.now())+'\r'
        session_file.write(log_session_to_file)      
        session_file.close()
    else:
        print(datetime.now(),'- Not Yet!!!, Will Try Again In 30mins')
    
    driver.close()

    time.sleep(1800)