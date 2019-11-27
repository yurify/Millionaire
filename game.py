import question_bank
import random

#questions = [question_bank.get_question(0), question_bank.get_question(0), question_bank.get_question(0), question_bank.get_question(0)]
prize = [100, 300, 500, 1000]
level = 0

print("Welcome to the game 'Who wants to be a millionaire?'\nLet's start the game!")

while level < 4:

    q = question_bank.get_question(level)

    print("Question number", level+1,". You can win", prize[level],"$!\n ***\n", q[0])
    print("A:", q[1])
    print("B:", q[2])
    print("C:", q[3])
    print("D:", q[4])

    user_answer = input("Please enter your choice: ")
    
    if user_answer == 'A' or user_answer == 'a':
        if q[1] == q[5]:
            print("Your answer is correct! You won: ", prize[level])
            level += 1
        else:
            print("Game over! Try once again.")
            level = 0
        
    elif user_answer == 'B' or user_answer == 'b':
        if q[2] == q[5]:
            print("Your answer is correct! You won: ", prize[level])
            level += 1
        else:
            print("Game over! Try once again.")
            level = 0

    elif user_answer == 'C' or user_answer == 'c':
        if q[3] == q[5]:
            print("Your answer is correct! You won: ", prize[level])
            level += 1
        else:
            print("Game over! Try once again.")
            level = 0

    elif user_answer == 'D' or user_answer == 'd':
        if q[4] == q[5]:
            print("Your answer is correct! You won: ", prize[level])
            level += 1
        else:
            print("Game over! Try once again.")
            level = 0

    else:
        print("Please enter A, B, C or D")

print("You won the game. Incredible!!!")
