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
Opdracht 3: Inventory
``` python
masterInv = []
 
def invQuestion():
    global masterInv
    for x in range(1,1000):
        item = input("Which item do you want to add to the inventory?: ").lower()
        quan = input(f"How many {item} do you want to add?: ").lower()
        desc = input(f"Describe {item}: ").lower()
 
        itemDict = {
            "name": item,
            "quantity": quan,
            "description": desc
        }
        masterInv.append(itemDict)
 
        change = input("Do you want to change the quantity of one of your items?: ").lower()
 
        if change == "y".lower():
            itemChange = input("Which item do you want to change?: ").lower()
            if itemChange == itemDict["name"]:
                lastChange = input(f"How many {itemChange} do you have now?: ").lower()
                itemDict.update({"quantity": lastChange})
 
        delete = input("Do you want to delete an item from your inventory? y/n: ").lower()
        if delete == "y".lower():
            delItem = input("Which item do you want to delete?: ").lower()
            for i in range(len(masterInv)):
                if masterInv[i]["name"] == delItem:
                    del masterInv[i]
                    break
 
        stop = input("Did you add all your items? y/n: ").lower() 
        if stop == "y".lower():
            break
 
invQuestion()
for x in masterInv:
    print(x)
```