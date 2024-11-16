import math
def show_balance(balance):
    print(f"Current balance is: ${balance:.2f}")

def deposit(balance):
    try:
        amount = float(input("Enter amount to be deposited: "))
        if amount < 0:
            print("Invalid Amount!")
            return 0
        print("\n Amount Deposited:")
        return amount
    except Exception as e :
        print("Transaction failed!")
        return 0
    # show_balance()

def withdraw(balance):
    try:
        amount = float(input("Enter amount to be withdrawn: "))
        if balance >= amount:
            print("\n Amount Withdrawn! \n Happy Banking!")
            return amount
        else:
            print("\n Insufficient balance !!.. ")
            print("\nTry Again With Lesser amount Or Check Balance")
            return 0
    except Exception as e :
        print("Transaction failed!")
        return 0
    # show_balance()

def main():
    f = open("balance.txt", "r")
    # f.write("##### Banking App #####")
    # f.seek(0)  # Move the file pointer to the beginning of the file
    # print(f.read())

    cred=[]
    cred=f.readlines()
    f.close()


    st=cred[1]
    c=st[0]
    idx=0
    for c in st:
        if c.isdigit():
            break
        idx+=1


    balance=float(st[idx:])
    # balance=0
    in_progress=True

    while in_progress:
        print("\n Welcome to Banking App")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            in_progress = False
            print("Thank you for using our banking app!")
        else:
            print("Invalid choice. Please try again.")


    cred.insert(1, f"Balance: {balance}\n")
    f = open("balance.txt", "w")
    # f.seek(0)
    f.writelines(cred)
    f.close()


if __name__ == "__main__":
    main()