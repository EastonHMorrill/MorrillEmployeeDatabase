import Person

MorePeople = True
People = []

File = open('File.txt', 'r')
Filelines = File.readlines()

for x in Filelines: 
    NewEmployee = Person.Person(x.split(" "))
    People.append(NewEmployee)

File.close()

menu = {}
menu['1']= "- Add Employee"
menu['2']= "- Delete Employee"
menu['3']= "- Edit Employee Information"
menu['4']= "- Exit Menu"

Bool = True

while Bool:
    options=menu.keys()
    for entry in options:
        print(entry, menu[entry])
    
    selection=input("Please Select 1-4: ")
    if selection =='1':
        print("\n Add: ")         ##\n should end the line
        NewEmployee = Person.Person()
        NewEmployee.getPerson()

    elif selection =='2':
        print("\n Delete: ")
        print("Who would you like to remove? (First and Last name): ")      
        firstname, lastname = input().split(" ")
        for emp in People:
            if(emp.firstname == firstname and emp.lastname == lastname):
               People.remove(emp)

    elif selection =='3':
        print("\n Edit: ")
        print("Who would you like to edit? (First and Last name): ")      
        firstname, lastname = input().split(" ")
        for emp in People:
            if(emp.firstname == firstname and emp.lastname == lastname):
               People.append(emp)

        newmenu={}
        newmenu['1']= "- Edit Firstname"
        newmenu['2']= "- Edit Lastname"
        newmenu['3']= "- Edit Wage"
        newmenu['4']= "- Edit Hours"
        newmenu['5']= "- Finish Editing"

        NewBool = True

        while NewBool:
            options=menu.keys()
            for entry in options:
             print(entry, newmenu[entry])
    
            selection=input("Please Select 1-5: ")

            if selection == '1':
                firstname = input("\n Enter New Firstname: ")
                People.append(firstname)
            
            if selection == '2':
                lastname = input("\n Enter New Lastname: ")
                People.append(lastname)
            
            if selection == '3':
                wage = input("\n Enter New Wage: ")
                People.append(wage)

            if selection == '4':
                hours = input("\n Enter New Hours: ")
                people.append(Hours)

            if selection == '5':
                print("\n Finished Editing: ")


    elif selection =='4':
        print("\n Exit: ")
        File = open('File.txt', 'w')
        for x in range(len(People)):
            print(People[x])
        for emp in People:
            File.write(str(emp.firstname)+" "+str(emp.lastname)+" "+str(emp.wage)+" "+str(emp.hours)+"\n")
        File.close()
        Bool = False
        


    else:
        print("Please Select 1-4:")


