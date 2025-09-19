customers = {}

# code for Register Customer option

def register_customer(customers):

    while True:

        phone = input("Enter your phone number :")

        if phone in customers:

            print("Customer already registered!")

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
        "purchase" : 0
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

            if(amount <= 0):

                print("Purchase amount must be positive!")
    
            else:

                print("Purchase recorded successfully!")

        except ValueError:

            print("Invalid input! Please enter a valid number.")


        purchase_amount = int(amount * 100)     # storing price in paise i.e, if input =1234.55 then it will become 123455 paise

        point = purchase_amount // 10000        # 100rupees = 1 point ; so 10000 paise = 1 point

        print(f"\nTotal purchase: ₹{purchase_amount/100:.2f}/-") #paise/100 = rupees .2f so that always it will be in two decimal places as in real-life bills

        customers[phone]["purchase"] += purchase_amount

        customers[phone]["point"] += point


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

        print(f"Total Purchase : {customers[phone]["purchase"]/100:.2f}")

        print(f"Reward Points Earned : {customers[phone]["point"]}")
        print("-------------------------------------------")


# code for redeem points

def redeem_points(customers):

    phone = input("Enter your phone number :")

    if phone not in customers:

        print("\nCustomer not registered!")

    else:

        redeem = int(input("Enter the points you wish to redeem:"))

        if redeem > customers[phone]["point"]:

            print("Insufficient Point Balance!")
            print("Check your point balance and redeem again!")

        else:

            customers[phone]["point"] -= redeem

            print(f"Redeemed {redeem} points. Discount = ₹{redeem}")
            print(f"Remaining points = {customers[phone]['point']}")
             



# code for MENU and conditions

print("-------------------------------------")
print("  Welcome to Loyalty+ Reward System")
print("-------------------------------------")

while True:

    print("\nMENU:\n1. Register Customer\n2. Record Purchase\n3. Show Customer Details\n4. Redeem Points\n5. View Balance\n6. Exit")

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

        print("Check Balance")

    elif choice == "6":

        print("\nThank you for using the Reward System!")

        break

    else:

        print("Invalid Choice. Please try again.")



