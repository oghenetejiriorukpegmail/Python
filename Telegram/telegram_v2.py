from telethon import TelegramClient
from telethon import events
import os, re
import time
import asyncio
import configparser

os.chdir('C:\\Users\\miner\\Documents\\Python\\Telegram')

config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']
win_count = 0
loss_count = 0


client = TelegramClient('binarex_robot', api_id, api_hash)

@client.on(events.NewMessage())
async def my_event_handler(event):
    with open('results.csv', 'a') as f:
        if "1518994770" in str(event.peer_id):
    #        print (event.text)
            event_list = event.text.strip().lower().split()
            print(event_list)
    #        print('prepare' in event.text.lower(),'prepare')
    #        print('signal' in event.text.lower(),'signal')
    #        print('summary' in event.text.lower(),'summary')
            if "prepare" in event.text.lower():
                print("Curency: ",str(event_list[3])[2:6]+str(event_list[3])[8:])
                f.write(str(event_list[3])[2:6]+str(event_list[3])[8:]+', ')
            elif "signal" in event.text.lower():
    #            print ('signal in event.text')
                if "safe" in event.text.lower():
    #                print ('safe in event.text')
                    print('Action:', re.sub(r'[()]','',str(event_list[4])).upper()+',', "Duration:", event_list[12])
                    f.write('0, ')
                else:
                    print('Action:', re.sub(r'[()]','',str(event_list[2])).upper()+',', "Duration:", event_list[5])
            elif "summary" in event.text.lower():
    #            print('summary in the list')
                if "safe" in event.text.lower():
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