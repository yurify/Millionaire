import random
import time
import pyttsx3

help50_used = False
audience_used = False
call_used = False

q00 = ['Your favorite programming language:', 'python', 'cobra', 'go', 'c++', 'python']
q01 = ['We live on:', 'Mars', 'Sun', 'Earth', 'Jupiter', 'Earth']
q02 = ['The most popular website', 'Google', 'Goggles', 'Googel', 'Gugil', 'Google']


def help50(question):
    global help50_used
    print("Computer, please remove 2 incorrect answers...")
    time.sleep(3)
    if help50_used == False:
        counter = 0
        while counter < 2:
            i = random.randint(1,4)
            #print(i)
            if question[i] == question[5]:
                continue
            elif question[i] == '':
                continue
            else:
                question[i] = ''
                counter += 1
    else:
        print("Sorry, this lifeline has been already used")
    help50_used = True

    
    

def audience():
    pass



name = "Наталя"

def call(n):
    

    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(voice, voice.id)
    #     engine.setProperty('voice', voice.id)
    #     engine.say("Hello World!")
    #     engine.runAndWait()
    #     engine.stop()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    
    # for voice in voices:
    #     engine.setProperty('voice', voice.id)
    engine.say('Hello!' + n)
    engine.say("I'm so glad to hear you!")

    engine.setProperty('voice', voices[1].id)
    engine.say("Yes, I am also glad")
    engine.runAndWait()


call(name)