from datetime import datetime
import webbrowser
import os, random

hello = ['hi','hello','hey','hie']
timeIntent = ['time please', 'tell me time',
              'what is the time', 'time']

while True:
    userMsg = input("Enter your message : ")
    userMsg = userMsg.lower()

    if userMsg in hello:
        print("Hello")
    elif userMsg in timeIntent:
        t = datetime.now().time()
        print("Time is",t)
    elif userMsg.startswith('open'):
        web = userMsg.split()[1]
        webbrowser.open(web+'.com')
    elif userMsg == "play music":
        path = "C:/Users/asus/Music"
        os.chdir(path)
        for root, folder, files in os.walk(path):
            song = random.choice(files)
            os.startfile(song)
    elif userMsg == "bye":
        print("Bye")
        break
    else:
        print("I don't understand")
