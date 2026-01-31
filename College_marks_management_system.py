try:
    print('Welcome to marks management system.')
    def list_dictionary(n,r,m):
        pl=[n,m]
        rool.append(r)
        main_list[r]=pl
        mark.append(m)
    x=int(input('enter how many students have to be taken='))
    main_list={}
    rool=[]
    mark=[]
    count=0
    sum=0
    print('Enter data of students:')
    for i in range(x):
        name = str(input('Name='))
        roll = int(input('Roll Number='))
        marks = int(input('Marks='))
        list_dictionary(name, roll, marks)
        count+=1
    t=str(input('Do you want to enter any another student data?(y/n)'))
    while t=='y' or t=='Y':
        name = str(input('Name='))
        roll = int(input('Roll Number='))
        marks = int(input('Marks='))
        list_dictionary(name, roll, marks)
        count+=1
        t=str(input('Do you want to enter another student data?(y/n)'))
    e=0
    for i in range(count):
        for j in range(i+1,count):
            if rool[i]==rool[j]:
                e=e+1
    if e>0:
        print('There are same roll numbers for both students.Check the data once.')
    else:
        sorted_list=dict(sorted(main_list.items(), key=lambda x:x[1][1], reverse=True))
        for i in range(count):
            sum=sum+mark[i]
        avg=sum/count
        print('All students data are=')
        for i in sorted_list.items():
            print(i)
        print('Topper=',next(iter(sorted_list.items())))
        print('Average marks=',avg)
        x=str(input('Do you want search any student marks(y/n)='))
        while x=='y' or x=='Y':
            roll_number=int(input('Enter your Roll Number='))
            print(sorted_list[roll_number])
            x = str(input('Do you want search any other student marks(y/n)='))
    print('Thank you for visiting marks management system.')
except:
    print('Sorry, please enter valid data.')