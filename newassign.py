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

def admin_acc():
    username=input("Enter admin username: ")
    password=input("Enter admin password: ")
    if username=="admin" and password=="admin":
        print("Menu")
        print("1.Make new account")
        print("2.Modify an Account")
        print("3.Delete an Account")
        print("Pick a Number from (1-3)")

        admin_num=int(input(" "))
        if admin_num==1:
            write_record()
        elif admin_num==2:
            #
        elif admin_num==3:
            #
        else:
            print("Invalid choice")
            continue

def customer_acc():
    print("1.check account details")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("Pick a number from (1-3)")
    admin_num=int(input(" "))
    if admin_num==1:
        search_record()



def main():
    print("Enter A for customer account \nEmter C for customer account")
    type_person=input(" ")
    if type_person =="A" or type_person=="a":
        admin_acc()
    elif type_person=="C" or type_person=="c":
        customer_acc()
    else:
        print("Emter Valid acc")

    



main()
