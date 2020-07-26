import datetime  # Importing the datetime library
import telepot   # Importing the telepot library
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
from time import sleep      # Importing the time library to provide the delays in program
import json
import requests
now = datetime.datetime.now() # Getting date and time

def find_movie(a):
    url1 = "http://omdbapi.com/?s="
    url2 = ""
    url3 = "&apikey=thewdb"
    url2 = a
    url = url1+url2+url3
    response = requests.get(url)
    #print(response.text)
    risp = response.json()
    #print risp.keys()
    if "Response" in risp.keys():
        print (risp['Search'][1])
    else:
        print ("cazz")
    return risp

def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    com = msg['text']   # Getting text from the message
    command = com.lower()
    print ('Received:', command)
    # Comparing the incoming message to send a reply according to it
    if command == '/hi':
        bot.sendMessage (chat_id, str("Hi! MakerPro"))
    elif command == '/time':
        bot.sendMessage(chat_id, str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
    elif command == '/date':
        bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
    elif "movie" in command:
        s = command[6:]
        risp = find_movie(s)
        Titolo = risp['Search'][1]['Title']
        Anno = risp['Search'][1]['Year']
        Immagine = risp['Search'][1]['Poster'] 
        bot.sendMessage(chat_id, str("Titolo film trovato: ") + Titolo + str(", ") + str("Anno uscita: ") + Anno + str(", ") + str("Immgine Poster: ") + Immagine)

# Insert your telegram token below
bot = telepot.Bot('202678137:AAETSgFM2Jm-N46cQbcgggyo24LgAKUE7Gs')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)
