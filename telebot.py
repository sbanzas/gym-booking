# importing all required libraries 
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
from telethon.sync import TelegramClient
from telethon.sessions import StringSession



api_id = '***REMOVED***'
api_hash = '***REMOVED***'
token = '***REMOVED***'

phone = '***REMOVED***'
session_string = "***REMOVED***"

def main():
	with TelegramClient(StringSession(), api_id, api_hash) as client:
	    print(client.session.save())
	    

if __name__ == "__main__":	
	main()
	

def sendfile(filepath):
	client = TelegramClient(session_string, api_id, api_hash) 
	try: 
		receiver1 = client.get_entity('@benru89')
		receiver2 = client.get_entity('@Acadesebi')
		client.send_file(receiver1, filepath) 
		client.send_message(receiver2, "Entretenme payaso y apuntate", parse_mode='html') 
		
	except Exception as e: 
		print(e); 
