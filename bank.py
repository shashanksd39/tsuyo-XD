import pickle
def set_data():
    global name, address,ph_number,acctype,balance,customer,accnum
    name=input("Name: ")
    accnum=int(input("Enter account number: "))
    address=input("Address: ")
    ph_number=int(input("Phone Number: "))
    acctype=input("Account type: ")
    balance=input("Balance Amount: ")
    customer={}
    customer['Name']=name
    customer['Account number']=accnum
    customer['Address']=address
    customer['Phone number']=ph_number
    customer['Account']=acctype
    customer['Balance amount']=balance
    return customer

def display_data(customer):
    print("Name: ",customer['Name'])
    print("Account number:",customer['Account number'])
    print("Address: ",customer['Address'])
    print("Phone number: ",customer['Phone number'])
    print("Account type: ",customer['Account'])
    print("Balance: ",customer['Balance amount'])
    print()

def write_record():
    outfile=open('assign.dat','ab')
    pickle.dump(set_data(),outfile)
    outfile.close()

def read_record():
    infile=open('assign.dat','rb')
    while True:
        try:
            customer=pickle.load(infile)
            display_data(customer)
        except EOFError: break
    infile.close()

def search_record():
    infile=open("assign.dat",'rb')
    accnum=int(input("Enter account number to search: "))
    flag=False
    while True:
        try:
            customer=pickle.load(infile)
            if customer['Account number'] == accnum:
                display_data(customer)
                flag=True
                break
        except EOFError: break
    
    if flag==False:
        print('Account not found')
        print()
    infile.close()

def show_choice():
    print("Menu") 

    print("1.Make New Account")
    print("2.Display Accounts")
    print("3.Search a Account")
    print("4.deposit") #
    print("5.withdraw") #
    
    print("6. Exit")

def main():
    while (True):
        show_choice()
        choice = input("Enter choice (1-6): ")
        print()

        if choice == "1":
            write_record()
        elif choice == "2":
            read_record()
        elif choice == "3":
            search_record()



        elif choice == "6":
            break
        else:
            print("Invalid input")

main()






