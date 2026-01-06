import time


#shows the list of products with prodcut title code and price(DONE)
# asks the user for the product code(DONE)
# User enters product code it automatically goes to the cart and adds the item price to the balance(DONE)
# asks if the user wants to purchase another item and adds another (DONE)
# and if user types exit, it ends the transaction and returns the balance (DONE)
# if the item is out of stock, it notifies the user and asks for another selection ()
# returns change if there is any left after the transaction ()
#add menu at start with options to vend item, restock items, exit program ()
# then you can insert money

items = { #Lisitng of items in the vending machine with their stock levels
        'A1': {'name': "Fred's Eyeball", 'price': 5.50, 'stock': 2},
        'A2': {'name': "Quandale's Dingle??", 'price': 10.00, 'stock': 1},
        'A3': {'name': "Legendary Hero", 'price': 2.75, 'stock': 8},
        'A4': {'name': "Diamond Pickaxe", 'price': 7.00, 'stock': 3},
        'B1': {'name': "Zenyatta's Orb", 'price': 1.50, 'stock': 10},
        'B2': {'name': "Spiky Blue Shell", 'price': 2.25, 'stock': 6},
        'B3': {'name': "Companion Cube", 'price': 2.50, 'stock': 4},
        'B4': {'name': "Pokeballs", 'price': 4.00, 'stock': 24},
        'C1': {'name': "Crowbar", 'price': 1.75, 'stock': 3},
        'C2': {'name': "Web Shooters", 'price': 6.25, 'stock': 4},
        'C3': {'name': "A Frying Pan", 'price': 3.50, 'stock': 1},
        'C4': {'name': "Holy Hand Grenades", 'price': 4.00, 'stock': 5},
    }

usermoney = 0.0  #variable to store user money input
total_price = 0.0 #total price variable to keep track of the total cost of items selected
cartfinal = []  #list to keep track of items in the cart

def transaction():  #function to handle the transaction and change return
    global usermoney
    usermoney = float(input('How much do you have? '))
    while usermoney < total_price:
        usermoney = usermoney + float(input(f'You don\'t have enough money *${usermoney:.2f}*. Please add more funds.\n Add here: '))
    time.sleep(1)
    print(f'successfully paid ${usermoney:.2f}')
    change = usermoney - total_price
    time.sleep(1)
    print(f'Transaction complete! Your change is ${change:.2f}. Thank you for using the Vending Machine!')

def restock(): #Restock function to reset stock levels 
    global items
    items = {
        'A1': {'name': "Fred's Eyeball", 'price': 5.50, 'stock': 2},
        'A2': {'name': "Quandale's Dingle", 'price': 10.00, 'stock': 1},
        'A3': {'name': "Legendary Hero", 'price': 2.75, 'stock': 8},
        'A4': {'name': "Diamond Pickaxe", 'price': 7.00, 'stock': 3},
        'B1': {'name': "Zenyatta's Orb", 'price': 1.50, 'stock': 10},
        'B2': {'name': "Spiky Blue Shell", 'price': 2.25, 'stock': 6},
        'B3': {'name': "Companion Cube", 'price': 2.50, 'stock': 4},
        'B4': {'name': "Pokeballs", 'price': 4.00, 'stock': 24},
        'C1': {'name': "Crowbar", 'price': 1.75, 'stock': 3},
        'C2': {'name': "Web Shooters", 'price': 6.25, 'stock': 4},
        'C3': {'name': "A Frying Pan", 'price': 3.50, 'stock': 1},
        'C4': {'name': "Holy Hand Grenades", 'price': 4.00, 'stock': 5},
    }    
    return items

def redo(): #the function that asks if user wants to purchase another item
    another = input("Do you want to purchase another item? (yes/no): ").lower() 
    time.sleep(1)  # ^^^ asks if user wants to purchase another item ^^^

    if another == 'yes' or another == 'y':
        return vend_item() #repeats
    elif another == 'no' or another == 'n':
        print(f'Items in cart: {cartfinal}')
        print("Proceeding to transaction...")
        transaction() #displays itmes and ends transaction
    else:
        print("Please enter yes or no.")
        return redo()  #if input is invalid it asks again

def vend_item():
    global total_price
    print ("Available items:")
    time.sleep(1)
    for name, item in items.items():
        print(f"{name}: {item['name']} - ${item['price']} (Stock: {item['stock']})")
    print("\n")
    cart = input("Enter the product code of the item you want to purchase:").upper()

    if cart in items:
        if items[cart]['stock'] > 0: #checks for stock if stock > 0 THEN executes block of code
            cartfinal.append(items[cart]['name']) #adds item to cart
            total_price += items[cart]['price'] #increments total price
            items[cart]['stock'] -= 1 #removes one from stock
            time.sleep(1)
            print(f"{items[cart]['name']} added to cart. Total price: ${total_price:.2f}")  #displays total price
            time.sleep(1)
            print(f'Items in cart: {cartfinal}') #displays items in cart
            redo() #the redo function called to ask if user wants to purchase another item
            
        else:
            print(f"Sorry, {items[cart]['name']} is out of stock. Please choose another item.") #if stock is 0 it notifies user
            time.sleep(1)
            return vend_item()
    
    elif cart == 'RESTOCK':
        time.sleep(1)
        print(f"Restocking Items")
        time.sleep(2)
        restock()
        print(f"Items Restocked")

    else:
        print("Invalid product code. Please try again.")
        time.sleep(1)
        return vend_item()
    

          
vend_item()