# importing all required libraries 
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 


api_id = '***REMOVED***'
api_hash = '***REMOVED***'
token = '1454175959:AAE6A6opz00N7eA-U31htWhnnYvZin3xUHU'

phone = '***REMOVED***'


def sendfile(filepath):
	client = TelegramClient('session', api_id, api_hash) 
 
	client.connect() 
	if not client.is_user_authorized(): 
		client.send_code_request(phone) 
		client.sign_in(phone, input('Enter the code: ')) 

	try: 
		receiver1 = client.get_entity('@benru89')
		receiver2 = client.get_entity('@Acadesebi')

		client.send_file(receiver1, filepath) 
		client.send_message(receiver2, "Entretenme payaso", parse_mode='html') 
		
		
	except Exception as e: 
		
		# there may be many error coming in while like peer 
		# error, wwrong access_hash, flood_error, etc 
		print(e); 
		

	# disconnecting the telegram session 
	client.disconnect() 

	

