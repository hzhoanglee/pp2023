class Student:
    def __init__(self):
        self.__sId = int(input("Enter Student ID: "))
        self.__sName = input("Enter Student name: ")
        self.__sDOB = input("Enter Student DOB: ")
        self.__sGPA = 0
        self.__sisGPA = False

    def id(self):
        return self.__sId

    def name(self):
        return self.__sName

    def dob(self):
        return self.__sDOB

    def getGPA(self):
        return self.__sGPA

    def setGPA(self, gpa):
        self.__sisGPA = True
        self.__sGPA = gpa

    def printInfo(self):
        print("------------------------")
        print(f"Student ID: {self.__sId}")
        print(f"Student Name: {self.__sName}")
        print(f"Student DOB: {self.__sDOB}")
        if self.__sisGPA:
            print(f"GPA: {self.__sGPA}")