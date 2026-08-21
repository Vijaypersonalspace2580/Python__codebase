    def faculty_database(self):
        with open("faculty.csv","a",newline='') as faculty_write_file:
            faculty_writer = csv.DictWriter(faculty_write_file,fieldnames=['ID','NAME','DOB','GENDER','DEPARTMENT','EMAIL','PHONE_NO','QUALIFICATION','EXPERIENCE','JOINING_DATE','DESIGNATION','EMPLOYEE_TYPE'])
            if not self.file: # Header only at once if file not exist or file execute at first time
                faculty_writer.writeheader()
            faculty_writer.writerow({'ID':self.Id,
                                     'NAME':self.Name,
                                     'DOB':self.Dob,
                                     'GENDER':self.Gender,
                                     'DEPARTMENT':self.Department,
                                     'EMAIL':self.Email,
                                     'PHONE_NO':self.Phone_no,
                                     'QUALIFICATION':self.qualification,
                                     'EXPERIENCE':self.experience,
                                     'JOINING_DATE':self.joining_date,
                                     'DESIGNATION':self.designation,
                                     'EMPLOYEE_TYPE':self.employee_type})
            print("Faculty details saved in database successfully")
