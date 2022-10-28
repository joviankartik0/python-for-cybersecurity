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


    
        
        
        
