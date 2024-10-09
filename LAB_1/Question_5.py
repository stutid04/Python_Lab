items = [ ]
num_items = int(input("Enter the number of items"))
for i in range (num_items) :
    name = input ("'Enter the item name: ")
    quantity = float (input (f" Enter the quantity"))
    price_per_item = float(input("Enter the price per item"))
    total_price = quantity * price_per_item
    items.append((name, quantity, price_per_item,total_price))
    print("\n*********BILL********")
    print(f"{"Item name":<20} {'Item Quantity':<15} {' Item Price':<15}{"Total Price":<15}")
    print ("-"* 65)
    total_amount = 0
    for item in items:
        name, quantity, price_per_item, total_price =item
        print(f"{name:<20} {quantity:<15} {price_per_item:<15.2f} {total_price:<15.2f}")
        total_amount+= total_price
        print ("-"* 65)
        print(f"{' Total Amone- to be paid': <50}{total_amount:<15.2f}")