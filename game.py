import random, time
import question_bank
import lifelines

#questions = [question_bank.get_question(0), question_bank.get_question(0), question_bank.get_question(0), question_bank.get_question(0)]
prize = [100, 300, 500, 1000]
level = 0

print("Welcome to the game 'Who wants to be a millionaire?'\nLet's start the game!")
print("If you need a lifeline, just type \n50  - will remove 2 incorrect answers\ncall  - a call to your friend \nzal  - help of audience")
username = input("Please enter your name to start: ")


def new_question(lvl):
    generated_question = question_bank.get_question(lvl)
    return generated_question
    
def print_question(q):
    global level
    print("Question number", level+1,". You can win", prize[level],"$!\n ***\n", q[0])
    time.sleep(2.5)
    print("A:", q[1])
    print("B:", q[2])
    print("C:", q[3])
    print("D:", q[4])


def select_answer(q):
    global level

    user_answer = input("Please enter your choice: ")
    if user_answer == 'A' or user_answer == 'a':
        if q[1] == q[5]:
            print("Your answer is correct! You won:", prize[level])
            level += 1
        else:
            print("Game over! Try once again.")
            level = 0
            time.sleep(2)
        
    elif user_answer == 'B' or user_answer == 'b':
        if q[2] == q[5]:
            print("Your answer is correct! You won:", prize[level])
            level += 1
        else:
            print("Game over! Try once again.")
            level = 0
            time.sleep(2)

    elif user_answer == 'C' or user_answer == 'c':
        if q[3] == q[5]:
            print("Your answer is correct! You won:", prize[level])
            level += 1
        else:
            print("Game over! Try once again.")
            level = 0
            time.sleep(2)

    elif user_answer == 'D' or user_answer == 'd':
        if q[4] == q[5]:
            print("Your answer is correct! You won:", prize[level])
            level += 1
        else:
            print("Game over! Try once again.")
            level = 0
            time.sleep(2)

    elif user_answer == '50' or user_answer == 'call' or user_answer == 'zal':
        if user_answer == '50':
            after50 = lifelines.help50(q)
            print_question(after50)
            select_answer(after50)
        
        elif user_answer == 'call':
            lifelines.call(username, q) 
            select_answer(q)       
        
        elif user_answer == 'zal':
            lifelines.audience(q)
            select_answer(q)

    else:
        print("Please enter A, B, C, D or you can use a lifeline(Just type: zal, call or 50)")
        select_answer(q)


while level < 4:
    question = new_question(level)
    print_question(question)
    select_answer(question)

print("You won the game. Incredible!!!")
time.sleep(1)

print("*************************CONGRATULATIONS!!!!*************************")
time.sleep(3)