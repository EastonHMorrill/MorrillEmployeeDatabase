#MorrillEmployeeDatabase

import Person

MorePeople = True
People = []

File = open('File.txt', 'r')
Filelines = File.readlines()

for x in Filelines: 
    NewEmployee = Person.Person(x.split(" "))
    People.append(NewEmployee)

File.close()

#Ask for employee information

#Create a plain text file that has all of the relevant employee information

#Create a menu that will present the user options aboutwhat they may want to do 

menu = {}
menu['1']= "- Add Employee"
menu['2']= "- Delete Employee"
menu['3']= "- Find Employee"
menu['4']= "- Exit Menu"

Bool = True

while Bool:
    options=menu.keys()
    for entry in options:
        print(entry, menu[entry])
    
    selection=input("Please Select 1-4:")
    if selection =='1':
        print("     Add")
        NewEmployee = Person.Person()
        NewEmployee.getPerson()
        #Need to add to the text file

    elif selection =='2':
        print("     Delete")
        #Who would you like to delete? (Lastname)
        if input == Person.lastname():
            delete Person.row[]
        def Deleteline():


    elif selection =='3':
        print("     Edit")
        #Who's account would you like to edit? (Lastname)

    elif selection =='4':
        print("     Exit")
        Bool = False


    else:
        print("Please Select 1-4:")


