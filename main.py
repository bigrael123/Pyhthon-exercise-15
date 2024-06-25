print("Snack Bar")
products = ["1 - Brazillian fried chicken balls ", "2 - fried turnover ", "3 - Coffee ", "4 - Juice ", "5 - Finish"]
price = [5.00, 7.00, 4.00, 6.00]
for i in range (len(products)):
    if(i  <len(products)-1):
        
             print(f"{products[i]}- {price[i]}")
    else:
       print(products[i])
selected_product= 0
totalprice = 0
while(True):
    selected_product = int(input("Type a number to select your product: "))
    if(selected_product>len(products) or selected_product<1):
        print("Invalid product")
    else:
        if(selected_product == 5):
            print(f"That will be {totalprice}")
            break
        current_price = price[selected_product-1]

        print(f"You bought {products[selected_product - 1]} for R${current_price}")
        while(True):
             selected_quantity = int(input("How many do you want? "))
             if(totalprice>-1):
                totalprice = selected_quantity * current_price
                break
             else:
                 print("Invalid quantity, try again.")
        print(f"Select Finish to conclude your shopping or buy more.")
        
