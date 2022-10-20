# Python for cybersecurity
## Fundamentals
Opdracht 1: Insurance Company
``` python
company_name = input("Enter the name of the company>> ")

num_employees = input("Enter number of employees>> ")

location = input("Enter location(city, OR country, OR state)>> ")

lowest_price = input("Enter lowest price for a policy>> ")

highest_price = input("Enter highest price for a policy>> ")

print(f"We are {company_name} located in {location}. Our {num_employees} employees can help you find the policy that is right for you with policies ranging from ${lowest_price} to ${highest_price} per month!")
```
Opdracht 2: Guessing Game
``` python
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
```