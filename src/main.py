main_menu = ('1. View Menu/Place Orders', '2. View shopping cart', '3. Remove item(s) in shopping cart', '4. Payment/Check Out')

sub_menu = ('1. Choose the same category',  '2. Return to main menu')

exit_menu = ('1. Remove a item', '2. Continue Shopping', '3. Payment')

order_menu = ('1. View in category', '2. View in alphabetical order', '3. View in ascending price')

payment_menu = ('1. Confirm Payment and Check Out', '2. Return to Main Menu')

product_dict = {
    'Milk': {'Category': 'Dairy', 'Price': 2.30},
    'Butter': {'Category': 'Dairy', 'Price': 4.50},
    'Eggs': {'Category': 'Dairy', 'Price': 3.40},
    'Cheese Slices': {'Category': 'Dairy', 'Price': 3.15},
    'Evaporated Milk Creamer': {'Category': 'Dairy', 'Price': 1.40},
    'Milo': {'Category': 'Dairy', 'Price': 12.50},
    'Biscuits': {'Category':'Dairy','Price': 5.30},
    'Yogurt': {'Category': 'Dairy', 'Price': 0.95},
    'Bread': {'Category': 'Package Goods', 'Price': 2.70},
    'Cereal': {'Category': 'Package Goods', 'Price': 7.00},
    'Crackers': {'Category': 'Package Goods', 'Price': 3.10},
    'Chips': {'Category': 'Package Goods', 'Price': 2.60},
    'Raisin': {'Category': 'Package Goods', 'Price': 2.10},
    'Nuts': {'Category': 'Package Goods', 'Price': 2.00},
    'Green Bean': {'Category': 'Package Goods', 'Price': 1.05},
    'Barley': {'Category': 'Package Goods', 'Price': 1.05},
    'Tomato': {'Category': 'Canned Goods', 'Price': 1.45},
    'Button Mushroom': {'Category': 'Canned Goods', 'Price': 1.15},
    'Baking Bean': {'Category': 'Canned Goods', 'Price': 1.43},
    'Tuna Fish': {'Category': 'Canned Goods', 'Price': 1.45},
    'Kernel Corn': {'Category': 'Canned Goods', 'Price': 1.25},
    'Sardine Fish': {'Category': 'Canned Goods', 'Price': 1.10},
    'Chicken Luncheon Meat': {'Category': 'Canned Goods', 'Price': 1.95},
    'Pickled Lettuce': {'Category': 'Canned Goods', 'Price': 0.95},
    'Fine Salt': {'Category': 'Condiments/Sauces', 'Price': 0.80},
    'Sea Salt Flakes': {'Category': 'Condiments/Sauces', 'Price': 1.30},
    'Chicken Stock': {'Category': 'Condiments/Sauces', 'Price': 3.15},
    'Chilli Sauce': {'Category': 'Condiments/Sauces', 'Price': 2.65},
    'Oyster Sauce': {'Category': 'Condiments/Sauces', 'Price': 4.50},
    'Sweet Soy Sauce': {'Category': 'Condiments/Sauces', 'Price': 3.75},
    'Tomato Ketchup': {'Category': 'Condiments/Sauces', 'Price': 3.20},
    'Sesame Oil': {'Category': 'Condiments/Sauces', 'Price': 4.95},
    'Green Tea Conned 330 ML': {'Category': 'Drink & Beverages', 'Price': 15.00},
    'Blackcurrant Ribena 330 ML': {'Category': 'Drink & Beverages', 'Price': 31.00},
    '100 Plus 24 Cans': {'Category': 'Drink & Beverages', 'Price': 15.00},
    'Orange Cordial 2 Litre': {'Category': 'Drink & Beverages', 'Price': 3.90},
    'Mineral Water 24 x 600ML': {'Category': 'Drink & Beverages', 'Price': 7.00},
    'Pineapple Juice': {'Category': 'Drink & Beverages', 'Price': 0.80},
    'Nescafe Coffee': {'Category': 'Drink & Beverages', 'Price': 9.90},
    'Coke 24 Cans': {'Category': 'Drink & Beverages', 'Price': 12.40}
}

shoppinglist = {}
price_ = []
num_in_dict = len(product_dict)


def display_main_menu():
    print('-'*30)
    print(f"{'Main Menu':>17}")
    print('-'*30)
    for item in main_menu:
        print(item)


def sort(sorted_list):
    print('-'*100)
    print(f"{'No.' :<10} {'|Item' : <30}{'|Category':^14}{'|Price exclusive of 7% GST' : >41}")
    print('-'*100)
    num = 1
    for key, value in sorted_list:
        cate = value['Category']
        price = value['Price']
        print(f"{num :<10} |{key:<30} |{cate:<25} |${price:<10.2f}")
        num += 1
    while True:
        try:
            i = int(input('Which item you want?:'))
            if (i > 0) and (i <= num_in_dict):
                i2 = i - 1
                price_ = sorted_list[i2][1]['Price']
                product_name = sorted_list[i2][0]
                cat = sorted_list[i2][1]['Category']
                quantity_ = int(input('What your quantity?:'))
                total = float(quantity_ * price_)
                print('')
                print('%s has been added into the cart. Quantity is %d. Total cost is $%.2f.' % (product_name, quantity_, total))
                shoppinglist.update({product_name: {'Category': cat, 'Quantity': quantity_, 'Price': total}})
                view_sub_menu()
            else:
                print(f"Please enter within the 1-{num_in_dict}. Try again.")
                print()
        except ValueError:
            print(f"Please enter a number. Try again.")
            print()


def sort_category():
    sorted_list = sorted(product_dict.items(), key=lambda x: x[1]['Category'])
    sort(sorted_list)


def sort_alphabetical():
    sorted_list = sorted(product_dict.items(), key=lambda x: x[0])
    sort(sorted_list)


def sort_price():
    sorted_list = sorted(product_dict.items(), key=lambda x: x[1]['Price'])
    sort(sorted_list)


def view_sub_menu():
    while choice == 1:
        for item in sub_menu:
            print(item)
        try:
            choice_2 = int(input('Please enter your option:'))
            if choice_2 == 1:
                if menu_choice == 1:
                    sort_category()
                elif menu_choice == 2:
                    sort_alphabetical()
                elif menu_choice == 3:
                    sort_price()
            elif choice_2 == 2:
                main()
            else:
                print('Please enter 1 or 2.')
                print('')
        except ValueError:
            print('Please enter 1 or 2.')
            print('')


def view_menu():
    for i in order_menu:
        print(i)
    global menu_choice
    while True:
        try:
            menu_choice = int(input('Please enter your option:'))
            if menu_choice == 1:
                sort_category()
            elif menu_choice == 2:
                sort_alphabetical()
            elif menu_choice == 3:
                sort_price()
            else:
                print('Please enter 1 - 3. Try again')
                print()
        except ValueError:
            print('Please enter 1 - 3. Try again')
            print()


def view_order():
    if shoppinglist == {}:
        print('No item has been added')
    else:
        print()
        print('-'*100)
        print(f"{'No.' :<10} {'|Item' : <20}{'|Category': <25}{'|Quantity':<15}{'|Price exclusive of 7% GST' : >4}")
        print('-'*100)
        num = 1
        for key, value in shoppinglist.items():
            print(f"{num: <10}|{key: <20}|{value['Category']: <23} |{value['Quantity']:<14}|${value['Price']: <10.2f}")
            num += 1
        print('-'*100)
        print()
    main()


def remove_orders():
    if shoppinglist == {}:
        print('No item has been added')
        print('')
        main()
    else:
        if shoppinglist == {}:
            print('No item has been added')
        else:
            print('')
            print('-'*100)
            print(f"{'No.' :<10} {'|Item' : <20}{'|Category': <25}{'|Quantity':<15}{'|Price exclusive of 7% GST' : >4}")
            print('-'*100)
            num = 1
            for key, value in shoppinglist.items():
                print(f"{num: <10}|{key[0:]: <20}|{value['Category']: <24}|{value['Quantity']:<14}|${value['Price']: <10.2f}")
                num += 1
            print('-'*100)
        num_in_shop = len(shoppinglist)
        while True:
            try:
                e = int(input('Which item need to remove?:'))
                if (e > 0) and (e <= num_in_shop):
                    e2 = e - 1
                    prod = list(shoppinglist.keys())[e2]
                    print("You have removed: " + prod)
                    del shoppinglist[prod]
                    print()
                    view_order()
                else:
                    print(f'Please enter within 0-{num_in_shop}. Try again.')
            except ValueError:
                print(f'Please enter within 0-{num_in_shop}. Try again.')


def payment():
    for i in payment_menu:
        print(i)
    while True:
        try:
            q = int(input('Please enter your option:'))
            if q == 1:
                print(f"{'Payment Successful':^90}")
                print(f"{'Thank You! Please come again.':^90}")
                exit()
            elif q == 2:
                main()
            else:
                print('Please enter 1 or 2. Try again.')
        except ValueError:
            print('Please enter 1 or 2. Try again.')


def display_receipt():
    print('-'*100)
    print(f"{'Order': ^90}")
    print(f"{'Bill Summary': ^90}")
    print('-'*100)
    print(f"{'No.' :<10} {'|Item' : <20}{'|Category': <25}{'|Quantity':<15}{'|Price exclusive of 7% GST' : >4}")
    print('-'*100)
    num = 1
    for key, value in shoppinglist.items():
        print(f"{num: <10}|{key: <20}|{value['Category']: <23} |{value['Quantity']:<14.0f}|${value['Price']: <10.2f}")
        num += 1
    print('-'*100)


def check_out():
    price_.clear()
    for value in shoppinglist.values():
        price_.append(value['Price'])
    total_sum = sum(price_)
    while True:
        discount = input('Do you have discount card? (y/n)')
        if discount == 'y':
            discount_total = total_sum * 0.9
            gst_total = discount_total * 1.07
            display_receipt()
            print(f"${total_sum:.2f}(Total cost of item ordered)")
            print(f"${discount_total:.2f}(with Discount of 10%)")
            print(f"${gst_total:.2f}(Final price GST of 7%)")
            print('-'*100)
            payment()
        elif discount == 'n':
            gst_total = float(total_sum * 1.07)
            display_receipt()
            print(f"${total_sum:.2f} {'(Total cost of item ordered)'} ")
            print(f"${gst_total:.2f} {'(Final price GST of 7%)'}")
            print('-'*100)
            payment()
        else:
            print('Please enter y or n.')
            continue


def main():
    display_main_menu()
    global choice
    while True:
        try:
            choice = int(input('Please enter your option:'))
            if choice == 1:
                view_menu()
            elif choice == 2:
                view_order()
            elif choice == 3:
                remove_orders()
            elif choice == 4:
                check_out()
            else:
                print('Please enter 1-4. Try again.')
                continue
        except ValueError:
            print('Please enter number 1-4.')


main()
