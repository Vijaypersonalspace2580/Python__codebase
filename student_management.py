import os
import csv
import re
from datetime import datetime as date
import random
from random import choice
if not os.path.exists("students.csv"):
    open("students.csv", "w", newline='').close()   # File not exist it can be created
file_exist=os.path.isfile("students.csv") and os.path.getsize("students.csv")>0     # chek file exist and how many times
class Read_students_data:  # read students.csv file
    def read(self):
        with open("students.csv","r",newline='') as student_read_csv:
            reader=csv.DictReader(student_read_csv)
            student_data={}
            for i in reader:
                student_data[i["ID"]]=i
        return student_data
class Register_student(): # Register student in college
    def __init__(self,file,reader):
        self.reader = reader #Take data from object
        self.file=file
    def verify_Id(self): # ID verification
        while(True):
            self.id_list =list(self.reader.keys())
            self.Id =str("V" + str(date.today().year) + str(random.randint(1000, 9999)))# Generate ID for student
            self.valid=False
            for i in self.id_list:
                if(i==self.Id):
                    self.valid=True
            if self.valid!=True:
                return True
                break
    def verify_Name(self): # Verification of name
        while(True):
            self.Name = input("Enter Student Name:")
            name_pattern = r"^[A-Za-z]+[A-Za-z\s]*[A-Za-z]+$"
            if re.fullmatch(name_pattern, self.Name):
                return True
                break
            else:
                print("Error:Invalid name format.Try again")
    def verify_Dob(self): # Verify date of birth
        while(True):
            self.Dob = input("Enter Student Date of birth(dd-mm-yyyy):")
            try:
                birth_date = date.strptime(self.Dob, "%d-%m-%Y").strftime("%Y-%m-%d")
                birth_year =int( birth_date.split('-')[0])
                current_year = date.today().year
                age=current_year - birth_year
                if(age>=17 and age<=25 and birth_year<=current_year):
                    return True
                    break
                elif(birth_year>current_year):
                    print("Error:Invalid year.Try again")
                else:
                    print("Age is out of range.Age must between 17 and 25")
                    return False
                    break
            except ValueError:
                print("Error=Invalid Date Format(dd-mm-yyyy) ex:01-01-2000.Try again")
    def verify_Gender(self):   #verification of gender
        while(True):
            self.Gender = input("Enter Student Gender(Male,Female,Other):").lower()
            if(self.Gender=="male" or self.Gender=="female" or self.Gender=="other"):
                return True
                break
            else:
                print("Error:Invalid Gender.Try again")
    def verify_Department(self): # Department verification
        while(True):
            self.Department = input("Enter Student Department(CSE,ECE,EEE,OTHER):").lower()
            if(self.Department=="cse" or self.Department=="eee" or self.Department=="ece"):
                return True
                break
            elif self.Department=="other":
                print("We can provide only CSE,ECE,EEE")
                choice=input("Do you want to continue with CSE,ECE,EEE (yes/no):").lower()
                if choice=="no":
                    return False
                    break
            else:
                print("Error:Invalid Department.Try again")
    def verify_Year(self):  # Verify studying year
        while(True):
            try:
                self.Year = int(input("Enter Student Year(1,2,3,4):"))
                if(self.Year>=1 and self.Year<=4):
                    return True
                    break
                else:
                    print("Error:Invalid Year.Try again")
            except ValueError:
                print("Error: Invalid input data.Try again")
    def verify_Email(self): # Email verification
        while(True):
            self.Email = input("Enter Student Email(ex:abc123.@gmail.com):").lower()
            email_pattern=r"^[a-z0-9]+(@gmail.com)$"
            if re.fullmatch(email_pattern,self.Email):
                return True
                break
            else:
                print("Error:Invalid Email ex:abc123.@gmail.com.Try again")
    def verify_Phone_no(self):  # Phone number verification
        while(True):
            self.Phone_no = input("Enter Student Phone No:")
            phone_no_pattern=r"\d{10}"
            if re.fullmatch(phone_no_pattern,self.Phone_no):
                return True
                break
            else:
                print("Error:Invalid Phone Number.Try again")
    def student_database(self):                   # Write all data in students.csv file
        with open("students.csv","a",newline='') as student_write_file:
            student_writer = csv.DictWriter(student_write_file,fieldnames=['ID','NAME','DOB','GENDER','DEPARTMENT','YEAR','EMAIL','PHONE_NO'])
            if not self.file: # Header only at once if file not exist or file execute at first time
                student_writer.writeheader()
            student_writer.writerow({'ID':self.Id,
                                     'NAME':self.Name,
                                     'DOB':self.Dob,
                                     'GENDER':self.Gender,
                                     'DEPARTMENT':self.Department,
                                     'YEAR':self.Year,
                                     'EMAIL':self.Email,
                                     'PHONE_NO':self.Phone_no})
            print("Student details saved in database successfully")
class Update_details():
    def __init__(self,reader):
        self.main_data=reader
        while True:
            self.details_list=["id",'name','dob','gender','department','year','email','Phone_no']
            for i in self.details_list:
                print(i.capitalize())
            self.choice=input("Enter which you want to update details:").lower()
            if self.choice=='id':
                print("Id not updated")
                self.option=input("Do you want to continue with another option(yes/no):")
                if(self.option!='yes'):
                    break
            elif self.choice in self.details_list[1::]:
                self.id=input("Enter Student ID:")
                if self.id in list(self.main_data.keys()):
                    if(self.choice=='name'):
                        while True:
                            self.old_name=input("Enter Student old Name:").lower()
                            name_pattern = r"^[A-Za-z]+[A-Za-z\s]*[A-Za-z]+$"
                            if re.fullmatch(name_pattern,self.old_name) and self.old_name==self.main_data[self.id]['NAME']:
                                while True:
                                    self.new_name=input("Enter Student new Name:").lower()
                                    if re.fullmatch(name_pattern,self.new_name) and self.new_name!=self.old_name:
                                        self.main_data[self.id]['NAME']=self.new_name
                                        break
                                    else:
                                        print("Error:Invalid Name format or your new name same as previous name.Try again")
                                break
                            else:
                                print("Error:Invalid Name format or name did not match with your previous name.Try again")
                    if(self.choice=='dob'):
                        while True:
                            self.old_dob = input("Enter Student old Date of birth(dd-mm-yyyy):")
                            if(self.old_dob==self.main_data[self.id]['DOB']):
                                while True:
                                    try:
                                        self.new_dob=input("Enter Student new Date of birth(dd-mm-yyyy):")
                                        birth_date = date.strptime(self.new_dob, "%d-%m-%Y").strftime("%Y-%m-%d")
                                        birth_year = int(birth_date.split('-')[0])
                                        current_year = date.today().year
                                        age = current_year - birth_year
                                        if (age >= 17 and age <= 25 and birth_year <= current_year) and self.new_dob!=self.old_dob:
                                            self.main_data[self.id]['DOB']=self.new_dob
                                            break
                                        elif (birth_year > current_year):
                                            print("Error:Invalid year.Try again")
                                        else:
                                            print("Age is out of range.Age must between 17 and 25 or your new DOB same as previous DOB")
                                    except ValueError:
                                        print("Error=Invalid Date Format(dd-mm-yyyy) ex:01-01-2000.Try again")
                                break
                            else:
                                print("Date of birth did not match with your previous DOB.Try again")
                    if(self.choice=='gender'):
                        while True:
                            self.old_gender = input("Enter Student old Gender:").lower()
                            if(self.old_gender==self.main_data[self.id]['GENDER']):
                                while True:
                                    self.new_gender=input("Enter Student new Gender:").lower()
                                    if(self.new_gender=='male' or self.new_gender=='female' or self.new_gender=='other') and self.new_gender!=self.old_gender:
                                        self.main_data[self.id]['GENDER']=self.new_gender
                                        break
                                    else:
                                        print("Error:Invalid Gender or your new gender same as previous gender.Try again")
                                break
                            else:
                                print("Gender will not match with previous Gender.Try again")
                    if(self.choice=='department'):
                        while True:
                            self.old_department = input("Enter Student old Department:").lower()
                            if(self.old_department==self.main_data[self.id]['DEPARTMENT']):
                                while True:
                                    self.new_department=input("Enter Student new Department:").lower()
                                    if(self.new_department=='cse' or self.new_department=='eee' or self.new_department=='ece') and self.new_department!=self.old_department:
                                        self.main_data[self.id]['DEPARTMENT']=self.new_department
                                        break
                                    else:
                                        print("Error:Invalid Department(Cse,Ece,Eee) or your new department same as previous department.Try again")
                                break
                            else:
                                print("Department cannot match with your previous Department.Try again")
                    if self.choice=='year':
                        try:
                            self.old_year = int(input("Enter Student old Year:"))
                            if(self.old_year==self.main_data[self.id]['YEAR']):
                                while True:
                                    self.new_year=int(input("Enter Student new Year:"))
                                    if(self.new_year>=1 and sel.new_year<=4) and self.new_year!=self.old_year:
                                        self.main_data[self.id]['YEAR']=self.new_year
                                        break
                                    else:
                                        print("Error:Invalid Year or your new year same as previous year.Try again")
                                break
                            else:
                                print("Year cannot match with your previous Year.Try again")
                        except ValueError:
                            print("Error:Invalid input.Try again")
                    if self.choice=='email':
                        email_pattern=r"^[a-z0-9]+(@gmail.com)$"
                        while True:
                            sel.old_email=input("Enter Student old Email:").lower()
                            if re.fullmatch(email_pattern,self.old_email) and self.old_email==self.main_data[self.id]['EMAIL']:
                                while True:
                                    sel.new_email=input("Enter Student new Email:").lower()
                                    if re.fullmatch(email_pattern,self.new_email) and self.new_email!=self.old_email:
                                        self.main_data[self.id]['EMAIL']=self.new_email
                                        break
                                    else:
                                        print("Error:Invalid Email format or your new email same as previous email.Try again")
                                break
                            else:
                                print("Your email cannot match with your previous Email.Try again")
                    if self.choice=='phone_no':
                        phone_no_pattern = r"\d{10}"
                        while True:
                            self.old_phone_no=input("Enter Student old Phone Number:")
                            if re.fullmatch(phone_no_pattern,self.old_phone_no) and self.old_phone_no==self.main_data[self.id]['PHONE_NO']:
                                while True:
                                    self.new_phone_no=input("Enter Student new Phone Number:")
                                    if re.fullmatch(phone_no_pattern,self.new_phone_no) and self.new_phone_no!=self.old_phone_no:
                                        self.main_data[self.id]['PHONE_NO']=self.new_phone_no
                                        break
                                    else:
                                        print("Error:Invalid Phone Number or it is equal to your previous phone number.Try again")
                                break
                            else:
                                print("Your phone_number cannot match with your previous Phone Number.Try again")
                    self.option=input("Do you want to update another details(yes/no):").lower()
                    if(self.option!='yes'):
                        break
                else:
                    print("Id not found")
                    self.option=input("Do you want to re enter again(yes/no):").lower()
                    if(sel.option!='yes'):
                        break
            else:
                print("Select perfect choice are given")
                self.option = input("Do you want to try again(yes/no):").lower()
                if (sel.option != 'yes'):
                    break
        with open("students.csv","w",newline='') as student_write_file:
            student_writer = csv.DictWriter(student_write_file,fieldnames=['ID','NAME','DOB','GENDER','DEPARTMENT','YEAR','EMAIL','PHONE_NO'])
            for i in self.main_data.keys():
                student_writer.writerow(self.main_data[i])
            print("Student details updated in database successfully")
def Register(register_obj):
    if register_obj.verify_Id() and register_obj.verify_Name() and register_obj.verify_Dob() and register_obj.verify_Gender() and register_obj.verify_Department() and register_obj.verify_Year() and register_obj.verify_Email() and register_obj.verify_Phone_no():
        register_obj.student_database()
    else:
        print("This student is not eligible for this college")
        print("I hope you are understand.Thank you")
obj=Read_students_data() # read the date of students.csv
read_data=obj.read()
Update_details(read_data)