# importing all required libraries 
import telebot 
import os
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 'API_ID'
API_HASH = 'API_HASH'
RECEIVER_USERNAME = os.environ.get('RECEIVER_USERNAME')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

SESSION_STRING = os.environ.get('SESSION_STRING')

def main():
    #Either get a normal session or a bot session
	with TelegramClient(StringSession(), API_ID, API_HASH) as client:
	    print(client.session.save())
	 
	
if __name__ == "__main__":	
	main()
	

def sendfile(filepath):
    if not SESSION_STRING: 
        client = TelegramClient('bot_name', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    else:
    	client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) 
    	client.connect() 

    receiver1 = client.get_entity(RECEIVER_USERNAME)
    client.send_file(receiver1, filepath) 	 
    client.disconnect()
