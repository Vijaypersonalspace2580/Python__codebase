try:
    phone_book = {}
    swapped_phone_book = {}
    def add_contacts():
        while True:
            name = input('Enter name: ')
            name = name.lower()
            phone_number = input('Enter phone number: ')
            if len(phone_number) == 10 and phone_number.isdigit()==True:
                if name not in phone_book and phone_number not in swapped_phone_book:
                    phone_book[name] = phone_number
                    swapped_phone_book[phone_number] = name
                else:
                    print('contact is exist')
                    continue
            else:
                print('Invalid phone number')
                continue
            break
    def search_contact():
        while True:
            choice = str(input('do you search by name or phone number(n/p): '))
            if choice == 'n':
                while True:
                    name = input('Enter name: ')
                    name = name.lower()
                    if name in phone_book:
                        print(name, phone_book[name])
                    else:
                        print("Contact not found")
                        continue
                    break
            elif choice == 'p':
                while True:
                    phone_number = input('Enter phone number: ')
                    if len(phone_number) == 10 and phone_number.isdigit() == True:
                        if phone_number in swapped_phone_book:
                            print(phone_number, swapped_phone_book[phone_number])
                        else:
                            print('phone number not found')
                            continue
                    else:
                        print('Invalid phone number')
                        continue
                    break
            else:
                print("Invalid choice")
                continue
            break
    def delete_contact():
        while True:
            choice = str(input('do you delete by name or phone number(n/p): '))
            if choice == 'n':
                while True:
                    name = input('Enter name: ')
                    name = name.lower()
                    if name in phone_book:
                        phone = phone_book[name]
                        del phone_book[name]
                        del swapped_phone_book[phone]
                        print('Contact deleted successfully')
                    else:
                        print('Contact not found')
                        continue
                    break
            elif choice == 'p':
                while True:
                    phone_number = input('Enter phone number: ')
                    if len(phone_number) == 10 and phone_number.isdigit() == True:
                        if phone_number in swapped_phone_book:
                            na = swapped_phone_book[phone_number]
                            del swapped_phone_book[phone_number]
                            del phone_book[na]
                            print('Contact deleted successfully')
                        else:
                            print('Contact not found')
                            continue
                    else:
                        print('Invalid phone number')
                        continue
                    break
            else:
                print("Invalid choice")
                continue
            break
    def update_contact():
        while True:
            choice = str(input('Do you update Name or Phone number(n/p): '))
            if choice == 'n':
                while True:
                    old_name = input('Enter old name: ')
                    old_name = old_name.lower()
                    if old_name in phone_book:
                        new_name = input('Enter new name: ')
                        if new_name not in phone_book:
                            new_name = new_name.lower()
                            phone=phone_book[old_name]
                            swapped_phone_book[phone] = new_name
                            del phone_book[old_name]
                            phone_book[new_name] = phone
                            print('Contact updated successfully')
                        else:
                            print('Name is Existed')
                    else:
                        print('Contact not found')
                        continue
                    break
            elif choice == 'p':
                while True:
                    old_phone = input('Enter old phone number: ')
                    new_phone = input('Enter new phone number: ')
                    if (len(old_phone) == 10 and old_phone.isdigit()) and (len(new_phone)==10 and new_phone.isdigit()==True)==True:
                        if new_phone not in swapped_phone_book:
                            if old_phone in swapped_phone_book:
                                nam=swapped_phone_book[old_phone]
                                phone_book[nam]=new_phone
                                del swapped_phone_book[old_phone]
                                swapped_phone_book[new_phone] = nam
                                print('Contact updated successfully')
                            else:
                                print('Contact not found')
                                continue
                        else:
                            print('Phone number is Existed')
                            continue
                    else:
                        print('Invalid phone number')
                        continue
                    break
            else:
                print('Invalid choice')
                continue
            break
    def display_contacts():
        for k,v in phone_book.items():
            print(k,v)
    n = int(input('Enter how many contacts do you add: '))
    print('Enter name and phone number:')
    for i in range(n):
        add_contacts()
    s = 'y'
    while (s == 'y' or s == 'Y'):
        print('1.Add contact')
        print('2.Search contact')
        print('3.Delete contact')
        print('4.Display all contacts')
        print('5.Update contact')
        print('6.Exit')
        option = int(input('Enter your option(1,2,3,4,5,6): '))
        if option == 1:
            add_contacts()
        elif option == 2:
            search_contact()
        elif option == 3:
            delete_contact()
        elif option == 4:
            display_contacts()
        elif option == 5:
            update_contact()
        elif option == 6:
            break
        else:
            print('Invalid option')
            continue
        s=str(input('Do yo want to choose another service(y/n): '))
except ValueError:
    print('Invalid input')
