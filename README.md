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
Deze opdracht heb ik samen met een medestudent gemaakt
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
Opdracht 4: Custom Packages
``` python
from opdracht_custom_package_classes import inventory
start = True
inventoryList = []

while start:
    try:
        question = input("\na: Add item \nb: Increase/Decrease quantity \nc: Delete item \nd: Check inventory \ne: Stop\nYour answer: ").lower()
        if question == "a":
            new_item = input("\nWhat item?\nYour answer: ").lower()
            new_description = input(f"\nDescribe {new_item}\nYour answer: ").lower()
            item = inventory(new_item, new_description)
            inventoryList.append(item)
        elif question == "b":
            question_b = input("\na: Increase\nb: Decrease\nYour answer: ").lower()
            if question_b == "a":
                answer_b = "+"
            else:
                answer_b = "-"
            item_name_quantity = input("\nWhat item?\nYour answer: ").lower()
            num = int(input("\nHow many?\nYour answer: "))
            for i in range(len(inventoryList)):
                if item_name_quantity == inventoryList[i].name:
                    inventoryList[i].quantity_change(answer_b, num)
                    if inventoryList[i].quantity >= 0:
                        inventoryList.pop(i)
        elif question == "c":
            item_delete = input("\nWhat item?\nYour answer: ").lower()
            inventory.delete_items(inventoryList, item_delete)
        elif question == "d":
            for i in range(len(inventoryList)):
                inventoryList[i].print_items()
        else:
            break
    except:
        print("\nSometing went wrong!")
```
``` python
class inventory:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.quantity = 1
    
    def quantity_change(self, operator, num):
        if operator == "+":
            self.quantity += num
        else:
            self.quantity -= num
    
    def print_items(self):
        print(f"\nName: {self.name}\nDescription: {self.description}\nQuantity: {self.quantity}\n")

    def delete_items(invList, name):
        for i in range(len(invList)):
            if name == invList[i].name:
                invList.pop(i)
                break  
        return invList
```
Opdracht 5: On your own
Deze opdracht heb ik samen met een medestudent gemaakt
``` python
import requests
import json

base_url = 'https://pokeapi.co/api/v2/pokemon/'
url_querry = input("Choose your pokemon: ")


r = requests.get(f'{base_url}{url_querry}')

resultName = r.json()["name"]

types = r.json()["types"]
resultType = types[0]["type"]
resultType = resultType["name"]

resultWeight = r.json()["weight"]

resultHeight = r.json()["height"]

resultMoves = r.json()["moves"]
resultMoves = len(resultMoves)

resultId = r.json()["id"]



print(f'name: {resultName}\n type: {resultType} \nweight: {resultWeight} \nheight: {resultHeight} \nid: {resultId} \nmove amount: {resultMoves}')
```