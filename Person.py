class Person:
    def __init__(self, firstname = "J.", lastname = "Doe", wage = 10.00, hours = 40.00):
        self.firstname = firstname
        self.lastname = lastname
        self.wage = wage
        self.hours = hours

    def getPerson(self):
        firstname, lastname = input("Hello! What is your full name?: ").split(" ")
        self.firstname = firstname
        self.lastname = lastname
        wage = input("What is your hourly wage? [$##.##]: ")
        self.wage = wage
        hours = input("How many hours did you work this week? [Estimate one decimal (##.#)]: ")
        self.hours = hours

    def setFirstname(self, firstname):
        self.firstname = firstname

    def setLastname(self, lastname):
        self.lastname = lastname

    def setWage(self, wage):
        self.wage = wage

    def setHours(self, hours):
        self.hours = hours
        