import pyttsx3
import speech_recognition as sr  #o modulo speech será representado por reco
import pywhatkit
import webbrowser
import datetime


print("Start")
vozAI = pyttsx3.init() # iniciar o modulo pyttsx3
ouvir = sr.Recognizer() # função que permite reconhecer a tua voz
vozAI.setProperty('rate',145)

vozAI.say("Hello I am lisa, what I can do for you?")
vozAI.runAndWait()

def big_main():
 with sr.Microphone() as source:
  MyVoice = ""
  ouvir.adjust_for_ambient_noise(source)
  MyVoice = ouvir.listen(source) # ouve o teu micro
  print("listen now...")
  try:
   command = ouvir.recognize_google(MyVoice) # pega no audio inserido no microfone e converte em string atraves da Api da google
   command = command.lower()
  except sr.UnknownValueError:
   vozAI.say("I dont know what you are saying, cant find that sounds on my database")
   vozAI.runAndWait()
   command="Not found"
  except sr.RequestError as ex:
   print("[ERROR:] " + ex)
  return command


while True:
 command = big_main()
 print(command)
 if "lisa" in command:
  command = command.replace("lisa","") # pega na string e remove a palavra lisa
  if "play" in command:
   song = command.replace("play","")
   pywhatkit.playonyt(song)
   vozAI.say("Alright sir")
   vozAI.runAndWait()
  elif "open chrome" in command or "open firefox" in command or "open opera" in command:
   webbrowser.open("https://google.com")
  elif "time" in command:
   horas = datetime.datetime.now().strftime('%H:%M')
   vozAI.say("Current time is" + horas)
   vozAI.runAndWait()
  elif "shut down yourself" in command or "become zero" in command:
   vozAI.say("goodbye sir, hope to see you next time soon")
   vozAI.runAndWait()
   break
  elif "do nothing" in command:
   print("não fiz nada")
  elif "search" in command:
   vozAI.say("what you want to seach for?")
   vozAI.runAndWait()
   search = big_main()
   google_url = "https://www.google.pt/search?q=" + search
   if search != "Not found":
    webbrowser.open(google_url)
    vozAI.say("alright sir")
    vozAI.runAndWait()
  elif "find location" in command:
   vozAI.say("what location you are thinking ?")
   vozAI.runAndWait()
   location = big_main()
   maps_url = "https://www.google.pt/maps/place/" + location
   if location != "Not found":
    webbrowser.open(maps_url)
    vozAI.say("alright sir")
    vozAI.runAndWait()
   else:
    vozAI.say("sorry, I didnt understand")
    vozAI.runAndWait()
  else:
   vozAI.say("Sorry, that command is unavailable")
   vozAI.runAndWait()
 else:
  print("Command doesnt exist")
