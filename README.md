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
(Deze opdracht heb ik samen met een medestudent gemaakt)
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
## Object Oriented Programming
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
## Let's make API requests
Opdracht 5: On your own
(Deze opdracht heb ik samen met een medestudent gemaakt)
``` python
import requests
import json
try:
    base_url = 'https://pokeapi.co/api/v2/pokemon/'
    url_querry = input("Choose your pokemon: ").lower()
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

    print(f'name: {resultName}\ntype: {resultType} \nweight: {resultWeight} \nheight: {resultHeight} \nid: {resultId} \nmove amount: {resultMoves}')
except:
    print("Something went wrong!")
```
Extra opdracht: Brawl Stars API
``` python
import requests
import json

myPlayerId = "28pv9q9p" 

def printCharacter(chosen):
    try:
        for k, v in chosen.items():
            if k == "gears":
                if len(v) == 10:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")" + ", " + v[5]["name"] + "(" + str(v[5]["level"]) + ")" + ", " + v[6]["name"] + "(" + str(v[6]["level"]) + ")" + ", " + v[7]["name"] + "(" + str(v[7]["level"]) + ")" + ", " + v[8]["name"] + "(" + str(v[8]["level"]) + ")" + ", " + v[9]["name"] + "(" + str(v[9]["level"]) + ")").lower()
                elif len(v) == 9:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")" + ", " + v[5]["name"] + "(" + str(v[5]["level"]) + ")" + ", " + v[6]["name"] + "(" + str(v[6]["level"]) + ")" + ", " + v[7]["name"] + "(" + str(v[7]["level"]) + ")" + ", " + v[8]["name"] + "(" + str(v[8]["level"]) + ")").lower()
                elif len(v) == 8:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")" + ", " + v[5]["name"] + "(" + str(v[5]["level"]) + ")" + ", " + v[6]["name"] + "(" + str(v[6]["level"]) + ")" + ", " + v[7]["name"] + "(" + str(v[7]["level"]) + ")").lower()
                elif len(v) == 7:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")" + ", " + v[5]["name"] + "(" + str(v[5]["level"]) + ")" + ", " + v[6]["name"] + "(" + str(v[6]["level"]) + ")").lower()
                elif len(v) == 6:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")" + ", " + v[5]["name"] + "(" + str(v[5]["level"]) + ")").lower()
                elif len(v) == 5:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")"  + ", " + v[4]["name"] + "(" + str(v[4]["level"]) + ")").lower()
                elif len(v) == 4:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")"  + ", " + v[3]["name"] + "(" + str(v[3]["level"]) + ")").lower()
                elif len(v) == 3:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")"  + ", " + v[2]["name"] + "(" + str(v[2]["level"]) + ")").lower()
                elif len(v) == 2:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")" + ", " + v[1]["name"] + "(" + str(v[1]["level"]) + ")").lower()
                elif len(v) == 1:
                    gears = (v[0]["name"] + "(" + str(v[0]["level"]) + ")").lower()
                else:
                    gears = ""
                print(f"{k}: {gears}") 
            elif k == "starPowers" or k == "gadgets":
                if len(v) == 2:
                    powerOrGadget = (v[0]["name"] + ", " + v[1]["name"]).lower()
                elif len(v) == 1:
                    powerOrGadget = (v[0]["name"]).lower()
                else:
                    powerOrGadget = ""
                print(f"{k}: {powerOrGadget}") 
            else:
                print(f"{k}: {v}")
    except:
        print("-")

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjliZjMyOGQyLTFmNDEtNDQwNC1iNTdjLWY0YWZjOGNkM2ZmZSIsImlhdCI6MTY2NzU1ODM0NCwic3ViIjoiZGV2ZWxvcGVyLzE4NmZlNWQ1LTFhOWQtN2YzMC00YjZlLTA4MTdjN2NhODk0ZSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiODcuMjA5LjM3LjM2Il0sInR5cGUiOiJjbGllbnQifV19.7GBb6ndRDM2mWOu1Si7dtZvlaUhnW_PAx2q1VEuO7AxghbvM406TDLNT5D_0iQQ8yCZ7zLpYRQxiNo00z5pN-A"
head = {'Authorization': 'Bearer {}'.format(token)}
base_url = "https://api.brawlstars.com/v1/"

question1 = input("Select what you want to see:\na: Brawlers\nb: Player information\nYour answer: ").lower()
if question1 == "a":
    r = requests.get(f"{base_url}brawlers", headers = head)
    charactersList = r.json()["items"]
    character = input("Type your brawler\nYour answer: ").upper()
    if character == "ALL": 
        try:
            for i in range(len(charactersList)):  
                print("")
                printCharacter(charactersList[i])
        except:
            print("-")
    else: 
        for i in range(len(charactersList)):
            if charactersList[i]["name"] == character:
                print("")
                printCharacter(charactersList[i])
elif question1 == "b":
    playerTag = input("type tag of the player: ")
    player = f"players/%23{playerTag}"
    r = requests.get(f"{base_url}{player}", headers = head)
    playerInfo = r.json()
    characersOrInfo = input("\na: Player Info\nb: All brawlers\nYour answer: ")
    print("")
    if characersOrInfo == "a": 
        for k, v in playerInfo.items():
            if k == "club":
                clubName = v["name"]
                print(f"{k}: {clubName}")
            elif k != "brawlers":
                print(f"{k}: {v}")
    else:
        for i in range(len(playerInfo["brawlers"])):
            printCharacter(playerInfo["brawlers"][i])
            print("")
```