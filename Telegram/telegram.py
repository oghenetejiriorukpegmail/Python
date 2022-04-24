from telethon import TelegramClient
import os
import time
import asyncio
import configparser

config = configparser.ConfigParser()
config.read("Telegram/config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']



client=TelegramClient(username,api_id,api_hash)
client.start(phone)

async def main():
    await client.get_messages()


with client:
    client.loop.run_until_complete(main())
