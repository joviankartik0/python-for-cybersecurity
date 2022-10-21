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