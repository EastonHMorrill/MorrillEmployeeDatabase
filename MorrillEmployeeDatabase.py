#MorrillEmployeeDatabase

import Person

MorePeople = True
People = []

File = Open('File.txt', 'r')
Filelines = File.readlines()

firstname = []
lastname = []
wage = []
hours = []

for x in Filelines: 
    firstname.append(x.split()[0])
    lastname.append(x.split()[1])
    float(wage.append(x.split()[2]))
    int(hours.append(x.split()[3]))

File.close

Print(firstname)


#Ask for employee information

#Create a plain text file that has all of the relevant employee information

#Create a menu that will present the user options aboutwhat they may want to do 