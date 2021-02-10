import Person

MorePeople = True
People = []

File = open('File.txt', 'r')
Filelines = File.readlines()

for x in Filelines: 
    info = x.split(" ")
    if (len(info) == 4):
        NewEmployee = Person.Person(info[0], info[1], info[2], info[3])
        People.append(NewEmployee)

File.close()

print(len(People))

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
        print("\n Add: ")
        NewEmployee = Person.Person()
        NewEmployee.getPerson()
        People.append(NewEmployee)

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
                
                NewBool=True

                newmenu={}
                newmenu['1']= "- Edit Firstname"
                newmenu['2']= "- Edit Lastname"
                newmenu['3']= "- Edit Wage"
                newmenu['4']= "- Edit Hours"
                newmenu['5']= "- Finish Editing"

                while NewBool:
                    options=newmenu.keys()
                    for entry in options:
                        print(entry, newmenu[entry])
    
                    selection=input("Please Select 1-5: ")

                    if selection == '1':
                        firstname = input("\n Enter New Firstname: ")
                        People.append(firstname)
            
                    elif selection == '2':
                        lastname = input("\n Enter New Lastname: ")
                        People.append(lastname)
            
                    elif selection == '3':
                        wage = input("\n Enter New Wage: ")
                        People.append(wage)

                    elif selection == '4':
                        hours = input("\n Enter New Hours: ")
                        people.append(hours)

                    elif selection == '5':
                        print("\n Finished Editing: ")
                        NewBool = False
                        break
                    
                    break
            else: 
                print("Please Select 1-5: ")

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
        print("Please Select 1-4: ")


