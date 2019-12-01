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
    if help50_used == False:
        print("Computer, please remove 2 incorrect answers...")
        time.sleep(3)
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
        help50_used = True
    else:
        print("Sorry, this lifeline has been already used")
        available_lifelines()
    return question
    
    

def call(name, question): 
    global call_used
    if call_used == False:
        probability = random.choice([question[5], question[5], question[5], question[5], question[1], question[2], question[3]])
        answer = str(probability)
        
        engine = pyttsx3.init()


        rate = engine.getProperty('rate')   # getting details of current speaking rate
        engine.setProperty('rate', 160)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)

        engine.say("Hello computer!")
        engine.say("We are calling you from a popular TV show Who wants to be a millionaire")
        time.sleep(1)
        engine.say(name + "needs your help")
        time.sleep(1)
        engine.say("so let me read the question")
        time.sleep(2)
        engine.say(str(question[0]))
        time.sleep(1)
        engine.say("Option A " + str(question[1]))
        time.sleep(0.5)
        engine.say("Option B " + str(question[2]))
        time.sleep(0.5)
        engine.say("Option C " + str(question[3]))
        time.sleep(0.5)
        engine.say("Option D " + str(question[4]))
        time.sleep(1)
        engine.say("You have 30 seconds to help " + name)

        engine.runAndWait()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        engine.say("Hello" + name)
        engine.say("I am so happy to hear you")
        time.sleep(1)
        engine.say("Let me think a moment")
        time.sleep(3)
        engine.say("I think the correct answer is")
        time.sleep(1)
        engine.say(answer)
        if answer == question[1]:
            engine.say("It's option A")
        elif answer == question[2]:
            engine.say("That's option B")
        elif answer == question[3]:
            engine.say("It should be option C")
        elif answer == question[4]:
            engine.say("This is option D")
        time.sleep(2)
        if answer == question[5]:
            engine.say("I'm one hundred percent sure that this answer is correct")
        time.sleep(1)
        engine.say("Good luck, " + name)

        engine.runAndWait()
        
        call_used = True
    else:
        print("You have already called a friend")
        available_lifelines()


def audience(question):

    global audience_used
    if audience_used == False:
        if question[5] == question[1]:
            first = random.randint(43, 78)
            second = random.randint(0, 100-first)
            third = random.randint(0, 100 - first - second)
            fourth = 100 - first - second - third     
        elif question[5] == question[2]:
            second = random.randint(46, 67)
            first = random.randint(0, 100-second)
            third = random.randint(0, 100 - first - second)
            fourth = 100 - first - second - third
        elif question[5] == question[3]:
            third = random.randint(34, 85)
            first = random.randint(0, 100 - third)
            second = random.randint(0, 100-first - third)
            fourth = 100 - first - second - third 
        elif question[5] == question[4]:
            fourth = random.randint(56, 63)
            first = random.randint(43, 100 - fourth)
            second = random.randint(0, 100-first - fourth)
            third = random.randint(0, 100 - first - second - fourth)

        # first = random.randint(0, 100)
        # second = random.randint(0, 100-first)
        # third = random.randint(0, 100 - first - second)
        # fourth = random.randint(0, 100 - first - second - third)
        print("Option A got {}%. Option B {}%, option C {}%. And option D {}%".format(first, second, third, fourth))
        audience_used = True        
    else:
        print("Sorry, you already used audience help")
        available_lifelines()


def available_lifelines():
    lifelines = (help50_used, audience_used, call_used)
    values = ("50/50", "Audience", "Call a friend")
    for x, y in zip(lifelines, values):
        if x == False:
            print(y, "= available", end=" ")
        else:
            print(y, "= used", end=" ")