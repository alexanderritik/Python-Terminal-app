import os  # for path
import pyttsx3 #enginw to speak somwthing
import speech_recognition as sr
import wikipedia
import webbrowser #to open webbrowser
import datetime,time
import random
import pygame
import requests
import json
import pydub

engine=pyttsx3.init()
voices=engine.getProperty('voices')

engine.setProperty('rate',139)
engine.setProperty('volume',1.0)
engine.setProperty('voice',voices[0].id)

def speak(string):
    engine.say(string)
    engine.runAndWait()



#for another text to speech module
#from win32com.client import Dispatch
#speak =Dispatch("SAPI.Spvoice")
#speak.Speak(string)
#engine.say(string)
#engine.runAndWait()

speak("IS there someone out there")
def wishme():
     tie=time.localtime()
     #hour=int(tie.tm_hour)
     hour=int(datetime.datetime.now().hour)
     if hour>=6 and hour<10:
        speak("good morning alexander ritik sir")
        speak("how can i help you")
     elif hour >=10 and hour <14:
        speak("good afternoon alexander ritik sir")
        speak("how can i help you")
     elif hour >=14 and hour <6:
        speak("good evening ritik sir")
        speak("I am jarvis how can i help you")

     else:
         speak("good evening ritik sir")
         speak("I am jarvis how can i help you")


r=sr.Recognizer()
def take():
   '''
    this function is use to take input form speaker
    '''
   print(sr.Microphone.list_microphone_names())
   #to connect to mic phone
   #mic=sr.Microphone()
   mic = sr.Microphone(device_index=1)
   #print(mic.device_index)
   #TO SELECT INPUT COME FROM MICROPHONE OR SPEAKER
   with mic as source:
      r.adjust_for_ambient_noise(source)
      print("listening ...")
      r.pause_threshold=1
      audio=r.listen(source)
      try:
          print("Recoginising...")
          query=r.recognize_google(audio,language="en-in")
          print(f"user said {query} \n")
          return query
      except Exception as e:
          print("you said nothing please try again \n")
          #for small time
          return " "



while True:
    query=take()
    query=query.lower()
    if 'jarvis' in query:
      query=query.replace('jarvis',"")
      wishme()
      while True:

        query=take()
        query=query.lower()
        print(query)

        if query=="no":
             speak("Thank you for using alexander.I hope you are have a nice day")
             break

        elif 'if there is why i will tell you' in query:
            speak("Because i an make your work easy")
            break

             #for wikipedia pip install wikipedia
        elif 'wikipedia' in query:
            r.pause_threshold=1
            print("Searching...")
            query=query.replace("wikipedia","")
            query=query.replace("search","")
            result=wikipedia.summary(query,sentences=5)
            speak("According to wikipedia")
            print(result)
            speak(result)
            print(f'https://en.wikipedia.org/wiki/{query}/')
            break

        elif 'what is' in query :
            r.pause_threshold=1

            print("Searching...")
            query=query.replace("what","")
            query=query.replace("is","")

            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
            print(f'https://en.wikipedia.org/wiki/{query}/')
            break

        elif 'about' in query:
            r.pause_threshold=1

            print("Searching...")
            query=query.replace("about","")
            query=query.replace("search","")
            result=wikipedia.summary(query,sentences=10)
            #to store in them in form of list
            re=result.split(".")
            for i in range(4):
                print(re[i])
                speak(re[i])

            speak("D you want to know more")
            r.pause_threshold = 1
            more=take().lower()

            if 'yes' in more:
                print(f'https://en.wikipedia.org/wiki/{query}/')
                for i in range(4, 11):
                    speak(re[i])

            else:
                speak("thank you for listening")

            break

        elif 'youtube' in query:
            #if in webbrowesr serach directly www.youtube.com it will open through  internet explorer bot if http:// thin open in googlechrome
            if 'search' in query:
                query = query.replace("search", "")
                query = query.replace("youtube", "")
                query = query.replace(" ", "+")
                query = query.replace("open", "")


                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                break
            else:
                webbrowser.open("https://www.youtube.com")
                break

        elif 'facebook' in query:
            query = query.replace("open", "")
            query = query.replace("facebook", "")
            webbrowser.open('https://www.facebook.com/?stype=lo&jlou=AfcZ2-2MnjukY74Q1QLv_k1PLY0huty1DxPvL7Zvs2r6ikDMPgxTSiaAzgJkFIrwmyXkE4YrTY5a-ZYzHwYjAD5RQRhqZzBU4u13j0IFY_drxg&smuh=35249&lh=Ac_RU2UFYhOKSTpD')
            break


        elif 'pornhub' in query:
            query = query.replace("pornhub", "")
            query = query.replace("open", "")
            webbrowser.open('https://www.pornhub.com/')
            break

        elif 'instagram' in query:
            query = query.replace("instagram", "")
            query = query.replace("open", "")
            webbrowser.open('https://www.instagram.com/')
            break

        elif 'hackerrank' in query:
            query = query.replace("hacker", "")
            query = query.replace("rank", "")
            query = query.replace("open", "")
            webbrowser.open('https://www.hackerrank.com/dashboard')
            break


        elif 'greek' in query:
            query = query.replace("greek", "")
            query = query.replace("open", "")
            query = query.replace("for", "")
            webbrowser.open('https://www.geeksforgeeks.org/')
            break

        elif 'school' in query:
            query = query.replace("w3", "")
            query = query.replace("open", "")
            query = query.replace("school", "")
            webbrowser.open('https://www.w3schools.com/')
            break

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            break

        elif 'satellite' in query:
            query = query.replace("view", "")
            query = query.replace("satellite", "")

            webbrowser.open(f'https://www.google.co.in/maps/search/{query}/@27.13191,83.5603103,2792m/data=!3m1!1e3')
            break

        elif 'map' in query or 'where is' in query:
            query = query.replace("city", "")
            query = query.replace("map", "")
            query = query.replace("where", "")
            query = query.replace("is", "")
            webbrowser.open(f"https://www.google.co.in/maps/search/{query}/@27.13191,83.5603103,15z")
            break

        elif 'play' in query and 'hindi' in query :
            music_dir = 'D:\Pics\pics\muxsic\hindi song'
            songs = os.listdir(music_dir)
            len=int(len(songs))
            lo=random.randint(0, len)
            os.startfile(os.path.join(music_dir, songs[lo]))




        elif 'play' in query and 'english' in query:
            music_dir='D:\\Pics\\pics\\muxsic\\English songs'
            os.chdir(music_dir)
            songs=os.listdir(music_dir)
            song=int(len(songs))
            son=random.randint(0,song)
            print(songs[son])
            file=songs[son]

            def music(file):
                pygame.mixer.init()
                pygame.mixer.music.load(file)
                pygame.mixer.music.set_volume(0.6)
                pygame.mixer.music.play()
                while True:
                    query=take().lower()
                    if 'stop'in query:
                        pygame.mixer.music.stop()
                        break
                    if 'next song' in query:
                        print("the song is changed")
                        son = random.randint(0, song)
                        print(songs[son])
                        file = songs[son]
                        music(file)
                    if 'low' in query:
                        print("voluume is decreased")
                        vol=0.5
                        vol=vol-0.3
                        pygame.mixer.music.set_volume(vol)
                    if 'up' in query:
                        print("volume is increased")
                        vol=0.5
                        vol=vol+0.1
                        pygame.mixer.music.set_volume(vol)


            music(file)
            break


        elif 'time' in query:
            tie = time.localtime()
            hour=str(tie.tm_hour)
            min=str(tie.tm_min)
            sec=str(tie.tm_sec)
            print(hour,min,sec)
            speak(f"the time is {hour} hour {min} min and {sec} sec")

        elif 'wamp' in query:
            wamp_dir = 'C:\wamp\wampmanager.exe'
            os.startfile(wamp_dir)
            break

        elif 'pycharm' in query or "python" in query:
            wamp_dir = '"C:\Program Files\JetBrains\PyCharm Community Edition 2017.1.4\bin\pycharm.exe"'
            os.startfile(wamp_dir)
            break

        elif 'news' in query and 'top' in query:
          try:
            url='https://newsapi.org/v2/top-headlines?country=in&apiKey=9b2c3bc64d2b4c24af8b65885a3a4534'
            top_news=requests.get(url).text
            top_news=json.loads(top_news)
            new=top_news["articles"]
            for news in new:
                print(news['source']['name'])
                print(news['title'])
                print(news['description'])
                print(news['url'])
                print(news['urlToImage'])
                print(news['publishedAt'])
                speak(str(news['title']))
            speak("Thats all about today top news ")
          except Exception as e:
              speak("There is problem in connection please tr again")


        elif 'news' in query and ('sport' in query or 'sports' in query):
          try:
            url='https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=9b2c3bc64d2b4c24af8b65885a3a4534'
            top_news=requests.get(url).text
            top_news=json.loads(top_news)
            new=top_news["articles"]
            for news in new:
                print(news['source']['name'])
                print(news['title'])
                print(news['description'])
                print(news['url'])
                print(news['urlToImage'])
                print(news['publishedAt'])
                speak(str(news['title']))
            speak("Thats all about today sports news ")
          except Exception as e:
              speak("There is problem in connection please tr again")


        elif 'news' in query and ('technology' in query or 'techno' in query):
          try:
            url='https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9b2c3bc64d2b4c24af8b65885a3a4534'
            top_news=requests.get(url).text
            top_news=json.loads(top_news)
            new=top_news["articles"]
            for news in new:
                print(news['source']['name'])
                print(news['title'])
                print(news['description'])
                print(news['url'])
                print(news['urlToImage'])
                print(news['publishedAt'])
                speak(str(news['title']))
            speak("Thats all about today technology news ")
          except Exception as e:
              speak("There is problem in connection please tr again")

        elif 'news' in query and 'health' in query :
          try:
            url='https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=9b2c3bc64d2b4c24af8b65885a3a4534'
            top_news=requests.get(url).text
            top_news=json.loads(top_news)
            new=top_news["articles"]
            for news in new:
                print(news['source']['name'])
                print(news['title'])
                print(news['description'])
                print(news['url'])
                print(news['urlToImage'])
                print(news['publishedAt'])
                speak(str(news['title']))
            speak("Thats all about today health news ")
          except Exception as e:
              speak("There is problem in connection please tr again")

        elif 'news' in query and 'entertainment' in query :
          try:
            url='https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=9b2c3bc64d2b4c24af8b65885a3a4534'
            top_news=requests.get(url).text
            top_news=json.loads(top_news)
            new=top_news["articles"]
            for news in new:
                print(news['source']['name'])
                print(news['title'])
                print(news['description'])
                print(news['url'])
                print(news['urlToImage'])
                print(news['publishedAt'])
                speak(str(news['title']))
            speak("Thats all about today entertainment news ")
          except Exception as e:
              speak("There is problem in connection please tr again")


        elif 'news' in query and 'science' in query :
          try:
            url='https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=9b2c3bc64d2b4c24af8b65885a3a4534'
            top_news=requests.get(url).text
            top_news=json.loads(top_news)
            new=top_news["articles"]
            for news in new:
                print(news['source']['name'])
                print(news['title'])
                print(news['description'])
                print(news['url'])
                print(news['urlToImage'])
                print(news['publishedAt'])
                speak(str(news['title']))
            speak("Thats all about today science news ")
          except Exception as e:
              speak("There is problem in connection please try again")


        elif 'convert' in query:
            import convert
            speak("you have converted successfully")

        elif 'download' in query and( 'audio'in query or 'video' in query):
            import u_tubedown
            speak("you have downloaded successfully ")

        elif 'english' in query and 'joke' in query:
            import engjoke
            from engjoke import joke
            speak(joke)

        elif 'railway' in query and 'information' in query:
            #Bookit is python code which i made it by using Railway API you can check its code
            import Bookit
            speak("THANk you for railway emquiry")


        elif 'weather' in query :
            import weatherapi

        elif ('send' in query or 'sent'in query) and 'email' in query :
            import gmailsent
            speak("You gmail has sent succesfully")



    elif "no" in query:
        speak("good bye")

    else :
        speak("say something")


