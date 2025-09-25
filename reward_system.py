
customers = {}


# code for Register Customer option

def register_customer(customers):

    while True:

        phone = input("Enter your phone number :")

        if phone in customers:

            print("Customer already registered!")
            return

        if not phone.isdigit():

            print("Invalid input! Only numbers are allowed.")

        elif len(phone) != 10:

            print("Phone number must be 10 digits.")

        else:

            print("Phone number stored.")
            break

    while True:

        name = input("Enter your name:").title()

        if not name.replace(" ","").isalpha():

            print("Name should contain only alphabets")

        else:

            print("Name Stored.")
            break

    customers[phone] = {

        "name" : name,
        "point": 0,
        "purchase" : []
    }

    print(f"{name} is registered successfully!")





# Code for Record Purchase option

def record_purchase(customers):

    phone = input("Enter your phone number :")

    if phone not in customers:

        print("Customer not registered!")
        print("Please register first to record your purchase.")

    else:

        try:

            amount = float(input("Enter the purchase amount:"))    # in rupees

        except ValueError:

            print("Invalid input! Please enter a valid amount.")

        else:

            if amount <= 0:

                print("Purchase amount must be positive!")
    
            else:

                customers[phone]["purchase"].append(amount)

                points_earned = int(amount // 100)  # every 100/- = 1 point 

                customers[phone]["point"] += points_earned


                print("Purchase recorded successfully!")

                print(f"\nTotal purchase: ₹{amount:.2f}")
                print(f"Reward points earned: {points_earned}")
                print(f"Total reward points: {customers[phone]['point']}")



# code for customer details

def customer_details(customers):

    phone = input("Enter your phone number :")

    if phone not in customers:

        print("\nCustomer not registered!")
        print("Please register first to view details.")

    else:

        print("-------------------------------------------")
        print("   Customer Details   ")
        print("-------------------------------------------")

        print(f"Customer Name : {customers[phone]["name"]}")

        print(f"Total Purchase : {sum(customers[phone]["purchase"]):.2f}")

        print(f"Reward Points Earned : {customers[phone]["point"]}")
        print("-------------------------------------------")


# code for redeem points

def redeem_points(customers):

    phone = input("Enter your phone number :")

    if phone not in customers:

        print("\nCustomer not registered!")
        
        print("Please register first to access great rewards!")

    else:

        balance = customers[phone]["point"]

        if balance == 0:

            print("No points to redeem")

        else:

            print(f"Your current reward point balance : {balance}")

            try:

                redeem = int(input("Enter the points you wish to redeem:"))

            except ValueError:

                print("Invalid Input! Enter a valid number.")

            else:

                if redeem <= 0:

                    print("Please enter a positive number of points to redeem.")
        
                elif redeem > balance:

                    print("Insufficient Point Balance!")
                    
                    print("Check your point balance and redeem again!")

                else:

                    last_purchase = customers[phone]["purchase"][-1]

                    if redeem > last_purchase:
                        
                        print(f"\nRedeem points cannot exceed your last purchase of ₹{last_purchase:.2f}")

                        redeem = int(last_purchase)


                    after_discount = last_purchase - redeem
                    
                    customers[phone]["purchase"][-1] = after_discount
                    
                    customers[phone]["point"] -= redeem

                    print(f"Redeemed {redeem} points. Discount = ₹{redeem}")
                    
                    print(f"Remaining points = {customers[phone]['point']}")
                    
                    print(f"\nTotal amount after discount = ₹{after_discount:.2f}")

            


# code to view balance reward points   

# def view_balance(customers):

#     phone = input("Enter your phone number :")

#     if phone not in customers:

#         print("\nCustomer not registered!")
#         print("Please register first and make purchase.")

#     else:

#         balance = customers[phone]["point"]
#         name1 = customers[phone]["name"]

#         print(f"\nCustomer: {name1}")

#         if balance == 0:

#             print("You dont have any reward points yet. Start shopping to earn points!")

#         else:

#             print(f"Balance Points : {balance}")




# code to view purchase history

def view_history(customers):

    phone = input("Enter your phone number :")

    if phone not in customers:

        print("\nCustomer not registered!")
        print("Please register first and make purchase.")

    else:

        history = customers[phone]["purchase"]

        if not history:

            print("No purchase records yet.")

        else:

            print(f"Customer: {customers[phone]["name"]}")
            print("\nPurchase History:")
            count = 1

            for price in history:
                
                
                print("-----------------")
                print(f"{count}. Rs.{price:.2f}")
                count += 1
            
            print("-----------------")
            print(f"\nTotal Purchase : ₹{sum(customers[phone]['purchase']):,.2f}")

                

# code to edit profile (name update only)

def edit_profile(customers):

    phone = input("Enter your phone number:")

    if phone not in customers:

        print("Customer not registered! Please register first.")

    else:

        print(f"Current Name: {customers[phone]["name"]}")

        while True:

            new_name = input("Enter new name:").title()

            if not new_name.replace(" ","").isalpha():

                print("Name should contain only alphabets.")

            else:

                customers[phone]["name"] = new_name

                print("New name updated successfully!")
                break




# code for listing all customer

def list_customers(customers):

    if customers == {}:

        print("No customers registered yet.")

    else:

        print(f"\nRegistered Customers Summary:")
        print("-------------------------------------------")

        for phone in customers:

            print("Phone", phone, "| Name:",customers[phone]["name"], "| Reward Points:",customers[phone]["point"])
            print("-------------------------------------------")



# code for MENU and conditions

print("-------------------------------------")
print("  Welcome to Loyalty+ Reward System")
print("-------------------------------------")

while True:

    print("\nMENU:\n1. Register Customer\n2. Record Purchase\n3. Show Customer Details\n4. Redeem Points\n5. View Purchase History \n6. Edit Profile \n7. List all customers \n8. Exit")

    choice = input("\nChoose Option:")

    if choice == "1":

        register_customer(customers)

    elif choice == "2":

        record_purchase(customers)

    elif choice == "3":

        customer_details(customers)

    elif choice == "4":

        redeem_points(customers)

    elif choice == "5":

        view_history(customers)

    elif choice == "6":

        edit_profile(customers)

    elif choice == "7":

        list_customers(customers)

    elif choice == "8":

        print("\nThank you for using Loyalty+ Reward System!")
        print("Have a great day!")

        break

    else:

        print("Invalid Choice. Please try again.")



