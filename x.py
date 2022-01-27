import pickle

def set_data():
    rollno= int(input('Enter roll number: '))
    name = input('Enter name: ')
    test_score = int(input('Enter test score: '))
    print()
    #create a dictionary
    student = {}
    student['rollno'] = rollno
    student['name'] = name
    student['test_score'] =test_score
    return student


def display_data(student):
    print('Roll number:', student['rollno'])
    print('Name:', student['name'])
    print('Test Score:', student['test_score'])
    print()

def write_record():
    outfile = open('student.dat',
    'ab')
    #serialize the object and writing to file
    pickle.dump(set_data(),
    outfile)
    #close the file
    outfile.close()

def read_records():
    infile = open('student.dat', 'rb')
#read to the end of file.
    while True:
        try:
#reading the oject from file
            student = pickle.load(infile)
#display the object
            display_data(student)
        except EOFError: break
#close the file
    infile.close()

def search_record():
    infile = open('student.dat', 'rb') 
    rollno =int(input('Enter rollno to search: ')) 
    flag = False
#read to the end of file.
    while True:
        try:
#reading the oject from file
            student = pickle.load(infile)
#display record if found and set flag
            if student['rollno'] == rollno:
                display_data(student)
                flag = True
                break

        except EOFError: break
    if flag == False:
        print('Record not Found') 
        print()
    infile.close()

def show_choices():
    print('Menu') 
    print('1.Add Record') 
    print('2.Display Records')
    print('3. Search a Record')
    print('4. Exit')

def main():
    while (True):
        show_choices()
        choice = input("Enter choice (1-6): ")
        print()
        if choice == "1":
            write_record()
        elif choice == "2":
            read_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            break
        else:
            print("Invalid input")

main()
