pincode = 1234

print("Enter your pincode, please: ")
user_pincode = int(input())

if pincode == user_pincode:
    print("How much money do you want to take?")
    amount = int(input())
else:
    print("Wrong pincode, please enter correct pincode. You have 2 attempts.")
    user_pincode = int(input())
    if pincode == user_pincode:
        print("How much money do you want to take?")
        amount = int(input())
    else:
        print("Wrong pincode, please enter correct pincode. You have 1 attempt.")
        user_pincode = int(input())
        if pincode == user_pincode:
            print("How much money do you want to take?")
            amount = int(input())
        else:
            print("Wrong pincode, your card is blocked.")