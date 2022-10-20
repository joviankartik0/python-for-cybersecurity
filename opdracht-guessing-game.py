import random

min_num = 1
max_num = 20
guess_limit = 10
random_num = random.randint(min_num, max_num)
check = False

print(f"Guess the number between {min_num} and {max_num}, you get {guess_limit} guesses")

for i in range(1,11):
    try:
        num_input = int(input(f"Guess {i}: "))
        if num_input == random_num:
            check = True
            break
        else:
            print("Wrong!")
    except:
        print("No letters!")

if check:
    print("You guessed the number correct!!")
    print(f"Guesses used: {i}")
else: 
    print(f"The correct number is {random_num}")