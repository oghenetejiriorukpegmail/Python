from email import message
from pydoc import cli
from telethon import TelegramClient
from telethon import events
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
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

async def main():
    client = TelegramClient('BINAREX_BOT', api_id, api_hash)
    await client.start()
    print(client.is_connected())
#   channel_messages = client.iter_dialogs(limit=1,ignore_pinned='yes')
    channel_username='cciephantom' # your channel
    channel_entity=await client.get_entity('https://t.me/joinchat/3AZWEmp2NYM4Mzc6')
    print (channel_entity)
    posts = await client(GetHistoryRequest(
        peer=channel_entity,
        limit=1,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))
    
    print (posts.messages)



    await client.run_until_disconnected()


asyncio.run(main())