# основна логіка гри:
# вітання 
# задається питання і 4 варіанти відповіді
# левел = 0
#  ВВЕДІТЬ ваш варіант
#  повідомлення АБО ви перемогли ДОДАТИ +1 левел
#  повідомлення АБО ви програли ГЕЙМ ОВЕР. 
# левел = 1
#  ВВЕДІТЬ ваш варіант
#  повідомлення АБО ви перемогли ДОДАТИ +1 левел
#  повідомлення АБО ви програли ГЕЙМ ОВЕР. 
# левел = 2
#  ВВЕДІТЬ ваш варіант
#  повідомлення АБО ви перемогли ДОДАТИ +1 левел
#  повідомлення АБО ви програли ГЕЙМ ОВЕР. 
q1 = ['Select the best color', 'green', 'yellow', 'blue', 'red', 'blue']
q2 = ['The best month ever', 'August', 'January', 'June', 'July', 'June']
q3 = ['We live on', 'Mars', 'Earth', 'Moon', 'Jupiter', 'Earth']
q4 = ['EPL club', 'Chelsea', 'Barcelona', 'Real', 'Dynamo', 'Chelsea']

questions = [q1, q2, q3, q4]
prize = [100, 300, 500, 1000]
level = 0


print("Welcome to the game 'Who wants to be a millionaire?'\nLet's start the game!")

while level < 4:


    print("Question number", level+1,". You can win", prize[level],"$!\n ***\n", questions[level][0])
    print("A:", questions[level][1])
    print("B:", questions[level][2])
    print("C:", questions[level][3])
    print("D:", questions[level][4])

    user_answer = input("Please enter your choice: ")
    
    if user_answer == 'A' or user_answer == 'a':
        user_answer = questions[level][1]
        if user_answer == questions[level][5]:
            print("Your answer is correct! You won: ", prize[level])
            level += 1
        else:
            print("Game over! Try once again. The correct answer was: ", questions[level][5])
            level = 0
        
    elif user_answer == 'B' or user_answer == 'b':
        user_answer = questions[level][2]
        if user_answer == questions[level][5]:
            print("Your answer is correct! You won: ", prize[level])
            level += 1
        else:
            print("Game over! Try once again. The correct answer was: ", questions[level][5])
            level = 0

    elif user_answer == 'C' or user_answer == 'c':
        user_answer = questions[level][3]
        if user_answer == questions[level][5]:
            print("Your answer is correct! You won: ", prize[level])
            level += 1
        else:
            print("Game over! Try once again. The correct answer was: ", questions[level][5])
            level = 0

    elif user_answer == 'D' or user_answer == 'd':
        user_answer = questions[level][4]
        if user_answer == questions[level][5]:
            print("Your answer is correct! You won: ", prize[level])
            level += 1
        else:
            print("Game over! Try once again. The correct answer was: ", questions[level][5])
            level = 0

    else:
        print("please enter A, B, C or D")
