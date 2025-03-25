accounts = {
        2002 : ["Vinod","06-06-2004","8304",50000],
        3003 : ["Ashok","16-06-2004","2304",80000],
        4004 : ["Subbu","07-01-2003",None,20000]
    }
print("Welcome !")
while True:
    print("##########*****************###########")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini Statement")
    print("5. Exit")
    x = int(input("Enter Your option: "))
    if x > 5:
        print("Choose the correct Option")
    else:
        if x == 1:
            acntno = int(input("Enter Account Number: "))
            if acntno not in accounts:
                print("No user exists with Account number")
            else:
                if accounts[acntno][-2] is None:
                    print("Generate Pin before withdraw operation")
                else:
                    pin = input("Enter Pin: ")
                    if accounts[acntno][-2] != pin:
                        print("Invalid Pin, Try again")
                    else:
                        amount = int(input("Enter Amount to Withdraw: "))
                        if amount <= accounts[acntno][-1]:
                            accounts[acntno][-1] -= amount
                            print("Withdraw Success")
                        else:
                            print("Insufficient Funds")
        elif x == 2:
            acntno = int(input("Enter Account Number: "))
            if acntno not in accounts:
                print("No user exists with Account number")
            else:
                amount = int(input("Enter Amount to be Deposited: "))
                accounts[acntno][-1] += amount
                print("Deposit Success")
        elif x == 3:
            acntno = int(input("Enter Account Number: "))
            if acntno not in accounts:
                print("No user exists with Account number")
            else:
                if accounts[acntno][-2] is not None:
                    print("Pin Already GEnerated")
                else:
                    pin = input("Enter Pin: ")
                    cpin = input("Re enter Pin: ")
                    if pin != cpin:
                        print("Pin Does not Match")
                    else:
                        accounts[acntno][-2] = pin
                        print("Pin Generated successfully !")
        elif x == 4:
            acntno = int(input("Enter Account Number: "))
            if acntno not in accounts:
                print("No user exists with Account number")
            else:
                if accounts[acntno][-2] is None:
                    print("Generate Pin before Mini statment operation")
                else:
                    pin = input("Enter Pin: ")
                    if accounts[acntno][-2] != pin:
                        print("Invalid Pin, Try again")
                    else:
                        print(f"Account Number: {acntno}")
                        print(f"Name: {accounts[acntno][0]}")
                        print(f"Date of Birth: {accounts[acntno][1]}")
                        print(f"Balance: {accounts[acntno][-1]}")
        else:
            print("Thank You")
            break
    print("#########***************##########")







            
