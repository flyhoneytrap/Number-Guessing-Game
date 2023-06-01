import random
print("Welcome to number guessing game.\nYou have to guess the number which computer has selected.\nThere are 4 difficulties. \nEasy, Normal and Hard.\nIn easy mode you will have 20 guesses\nIn Normal mode you will have 10 guesses\nIn Hard mode you will have only 5 guesses.\nIn Extreme mode you will have only 1 guess.\nThere is a 100 guesses mode too. You get 100 guesses to guess number.\n\nGood Luck.\n\nNumber will range from 1 to 100.\n\nFor 100 Guess mode enter 0.\nFor Easy mode Enter 1\nFor Normalj mode Enter 2\nFor Hard mode Enter 3\nFor Extreme mode Enter 4\nYour Choice: ")

while True:
    try:
        difficulty = int(input())
        if difficulty < 5 and difficulty > -1:
            break
        print("\nChoice Doesn't Exists. Try again: ")
        continue

    except Exception as e:
        print("\nEnter a valid Choice.\n")



ran_num = int(random.randrange(101))
if difficulty==1:
    turn = 20
elif difficulty == 2:
    turn = 10
elif difficulty == 3:
    turn = 5
elif difficulty == 4:
    turn = 1
elif difficulty == 0:
    turn = 100
score = 1
# print(ran_num)
print("Guesses Remaining:",turn)
while turn > 0:
    try:
        guess = int(input("Guess the Number: "))
    except Exception as e:
        print("Enter a Integer value")
        continue
    turn -= 1
    if guess == ran_num:
        print("Yay!!! You guessed the number correctly")
        print("You took",score,"tries.")
        exit()
    elif guess < ran_num:
        print("Go Higher. Guesses remaining",turn)
    elif guess > ran_num:
        print("Go Lower. Guesses remaining",turn)
    score += 1


print("You didn't guess correctly. The number was",ran_num)
