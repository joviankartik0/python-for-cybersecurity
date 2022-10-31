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
