import csv
import os
if not os.path.exists('marks.csv'):
    open('marks.csv', 'w').close()
def roll_num(number):
    with open('marks.csv', 'r') as f:
        reader = csv.reader(f,delimiter=',')
        roll_list=[]
        reader=list(reader)
        for i in reader:
            if len(i)>0:
                roll_list.append(int(i[0]))
        return number not in roll_list
def data_dict():
    main_dictionary={}
    with open('marks.csv', 'r') as f:
        reader=csv.reader(f,delimiter=',')
        reader=list(reader)
        for i in reader:
            if len(i)>0:
                key=int(i[0])
                value=[i[1],i[2]]
                main_dictionary[key]=value
    return main_dictionary
def add_marks():
    with open('marks.csv', 'a') as f:
        writer = csv.writer(f,delimiter=',')
        while True:
            try:
                roll = int(input('Enter roll number: '))
                name = input('Enter name: ')
                marks = int(input('Enter marks: '))
                if roll_num(roll):
                    writer.writerow([roll,name,marks])
                    break
                else:
                    print("Student roll number already exists")
            except ValueError:
                print("Enter valid input")
def avg_marks():
    with open('marks.csv', 'r') as f:
        reader = csv.reader(f,delimiter=',')
        reader = list(reader)
        total= 0
        count=0
        if len(reader)==0:
            print("File is empty")
        else:
            for i in reader:
                if len(i)>0:
                    total+= int(i[-1])
                    count+=1
            if count == 0:
                print("Student records not found")
            else:
                avg = total / count
                print("Average marks =", avg)
def view_data():
    with open('marks.csv', 'r') as f:
        reader = csv.reader(f,delimiter=',')
        reader = list(reader)
        if len(reader)==0:
            print("File is empty")
        else:
            for i in reader:
                if len(i)>0:
                    print("Roll Number:",i[0],"| Name:",i[1],'| Marks:',i[2])
def delete_marks():
    call_data = data_dict()
    print('1. Delete all')
    print('2. Delete particular student')
    try:
        choice = int(input("Select your choice: "))
    except ValueError:
        print("Enter valid choice")
        return
    if choice == 1:
        confirm = input("Are you sure to delete all records? (yes/no): ")
        if confirm.lower() == "yes":
            open('marks.csv', 'w').close()
            print("All records deleted successfully")
    elif choice == 2:
        try:
            roll = int(input("Enter roll number to delete: "))
            if roll in call_data:
                call_data.pop(roll)
                print("Student deleted successfully")
                with open('marks.csv', 'w') as f:
                    writer = csv.writer(f)
                    for key, value in call_data.items():
                        writer.writerow([key, value[0], value[1]])
            else:
                print("Student record not found")
        except ValueError:
            print("Enter valid roll number")
    else:
        print("Invalid choice")
def search_marks():
    data_dictionary={}
    with open('marks.csv', 'r') as f:
        reader = csv.reader(f,delimiter=',')
        reader = list(reader)
        if len(reader)==0:
            print("File is empty")
        else:
            for i in reader:
                if len(i)>0:
                    r=int(i[0])
                    mini_list=[i[1],i[2]]
                    data_dictionary[r]=mini_list
            try:
                roll_number =int(input('Enter your roll number: '))
                if roll_number in data_dictionary.keys():
                    nn,mm=data_dictionary[roll_number]
                    print("Name:",nn,"| Marks:",mm)
                else:
                    print('Student not found')
            except ValueError:
                print("Enter valid input")
def update():
    call_data=data_dict()
    while True:
        try:
            roll_number=int(input("Enter roll number: "))
            if roll_number in call_data.keys():
                while True:
                    print('1.Update name\n2.Update marks')
                    try:
                        choice=int(input('Enter your choice: '))
                        if choice==1:
                            name=input("Enter your name: ")
                            call_data[roll_number][0]=name
                            print('Update name successfully')
                            break
                        elif choice==2:
                            marks=input("Enter marks: ")
                            call_data[roll_number][1]=marks
                            print('Update marks successfully')
                            break
                        else:
                            print("Select valid choice")
                    except ValueError:
                        print("Enter valid input")
                break
            else:
                print("Student record not found")
        except ValueError:
            print("Enter valid input")
    with open('marks.csv', 'w') as f:
        writer=csv.writer(f,delimiter=',')
        for i in call_data.keys():
            roll=str(i)
            name=call_data[i][0]
            marks=call_data[i][1]
            writer.writerow([roll,name,marks])
print("Welcome to College Marks Management System")
while True:
    print("1.Add student record\n2.Delete Student records\n3.Average marks\n4.View student records\n5.Search student record\n6.Update student record\n7.Exit")
    try:
        n =int(input('Select your choice: '))
        if n == 1:
            add_marks()
        elif n == 2:
            delete_marks()
        elif n == 3:
            avg_marks()
        elif n == 4:
            view_data()
        elif n == 5:
            search_marks()
        elif n == 6:
            update()
        elif n==7:
            break
        else:
            print("Enter valid choice")
    except ValueError:
        print("Enter valid choice")