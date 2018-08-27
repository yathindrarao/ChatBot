# ChatBot
import chatterbot 
import os
import speech_recognition as sr
r=sr.Recognizer() # recognizes the speech
from chatterbot.trainers import ListTrainer # listtrainer trains the bot to give the appropriate reply 

bot=chatterbot.ChatBot('bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('G:/Yathindra/Python\chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('G:/Yathindra/Python\chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    bot.train(data)#the address of the files where the training list is kept
    
while True:
    with sr.Microphone() as source:
        audio=r.listen(source)#listens the audio
    try :
        message=r.recognize_google(audio)#detects the input and copy it to the message
        print("me: ",message)
        reply=bot.get_response(message)#ask the bot to get the appropriate answer to the question
        print('yathi: ',reply)
        if message.strip() == 'Bye':#if message is BYE quite the program
            print('GoodBye!!!!!')
            break
    except:
        pass
  
  
