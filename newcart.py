# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    cart_items = {}
    
    #Show Cart
    def show_cart (cart_items = cart_items):
        if len(cart_items) < 1: #gotcha
            print("Sorry! You have no items in your cart. \nTry adding some...")
        else:
            price_list = cart_items.values()
            total = sum(price_list)
            print("Your Cart:\n")
            for i in cart_items:
                print(i + " : " + str(cart_items[i]))
            print("Your Total is " + str(total))

    #Add to Cart   
    def add_to_cart (cart_items = cart_items):
        item = str(input("Whould item would you like to add to your cart?"))
        item_num = 1
        og_len = len(item)
        for i in cart_items:
            if item == i:
                item_num += 1
                item = "".join(c for c in item if c.isalpha())
                item = item + str(item_num)
        try:
            price = float(input("how much does it cost?")) 
            cart_items[item] = price
            price_list = cart_items.values()
            total = sum(price_list)
            print("Item Added!")
            print("your new total is " + str(total))
        except:
            print("Try entering your price as number please :)") #gotcha
        
            
    #Remove from Cart
    def remove_from_cart (cart_items = cart_items):
        if len(cart_items) < 1: #gotcha
            print("Sorry! You have no items in your cart. \nTry adding some...")
        else:
            item_count = 0
            cart_value_list = []
            for i in cart_items:
                item_count += 1
                cart_value_list.append(i)
                print(str(item_count) + ":" + i)
            try:
                item_number = int(input("Which Item Would you like to remove? \n (try typing the number to the left of the item)"))
                if item_number > item_count or item_number < 0:
                    print("Next time, try useing a number. \n(specifically one on the list...)")
                else: 
                    cart_items[cart_value_list[item_number - 1]] = 0.0
            except:
                print("Next time, try useing a number. \n(specifically one on the list)")

running = True
cart= Cart
print("What would you like to do?")
print("Show Cart (Type: 'show') \nRemove an Item in your cart (Type: 'remove') \nadd new item to cart(Type: 'add') \nQuit(Type: 'quit')\n")
while running == True:
    request = input("I would like to...\n").lower()
    if request == "show":
        cart.show_cart()        
    if request == "add":
        cart.add_to_cart()
    if request == "remove":
        cart.remove_from_cart()
    if request == "quit":
        running = False
    if request != "quit" and request != "show" and request != "remove" and request != "add":
        print("That doesnt seem right...")
        print("Try one of these: \n")
        print("Show Cart (Type: 'show') \nRemove an Item in your cart (Type: 'remove') \nadd new item to cart(Type: 'add') \nQuit(Type: 'quit')\n")
print("Byeeee")
