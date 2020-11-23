# importing all required libraries 
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = '12412314'
api_hash = 'fakeapi1231231238sdajsd2e6'
token = '123123123:AitstdaNFfakefakexc1token0'

phone = '+34666666665'
ruben_session_string = """GFakeSess¡IonStrringsasMBu04EQb2h406omBhFakeSess¡IonStrringsasdAUGSXSTlwFakeSess¡IonStrringsas9W2qhlGihxNU-j_ldPkpm64S6ZzEgh7o0hoFakeSess¡IonStrringsasT4WNof2z-3a-1IvF9tEnFgiYQjMvDVjPCyFakeSess¡IonStrringsasYODW3_rrQ-DoIUktFakeSess¡IonStrringsas_itB2ztrPatAiOVTjyfS1PCllyxW4-pbYPd71-3FakeSess¡IonStrringsasSL-QsMdj_8v0RKypgSJh047JHr_zAu-RR2wQ-FakeSess¡IonStrringsas8QmQlsQ4zCDH4="""

bot_session_string = """FakeSess¡IonStrringsasBfpQSFakeSess¡IonStrringsasXDjd1S2-NBiFakeSess¡IonStrringsasq2bFakeSess¡IonStrringsasPIJXc4ik5oirWCAHpXktkOnDYFakeSess¡IonStrrFakeSess¡IonStrringsas4lUT7u9NlLNh-7FakeSess¡IonStrringsasKEXFakeSess¡IonStrringsas-z4J8lNFdwv-LOK0WfKrXj1EaEj8mFakeSess¡IonStrringsaseQR0wztmLLLSxxfKFwFMlanjuqBtp76D9vg_ImBHWgjJFakeSess¡IonStrringsasciOIw2eqa4lzVVmb8="""

def main():
	with TelegramClient(StringSession(), api_id, api_hash) as client:
	    print(client.session.save())
	    

if __name__ == "__main__":	
	main()
	

def sendfile(filepath):
	client = TelegramClient(StringSession(bot_session_string), api_id, api_hash) 
	client.connect() 

	receiver1 = client.get_entity('@benru89')
	receiver2 = client.get_entity('@Acadesebi')
	client.send_file(receiver1, filepath) 
	#client.send_message(receiver2, "Entretenme payaso y apuntate", parse_mode='html') 
			 
	client.disconnect()
