# Defining the classes
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


class Course:
    def __init__(self):
        self.__cId = int(input("Enter Course ID: "))
        self.__cName = input("Enter Course Name: ")
        self.__cCredit = input("Enter Course credits: ")

    def getID(self):
        return self.__cId

    def getName(self):
        return self.__cName

    def getCredit(self):
        return self.__cCredit

    def printInfo(self):
        print("------------------------")
        print(f"Course ID: {self.__cId}")
        print(f"Course Name: {self.__cName}")
        print(f"Course Credit: {self.__cCredit}")


class MarksByCourse:
    def __init__(self, cID):
        self.course = cID
        self.__marks = {}

    def newMark(self, sID, mark):
        self.__marks[sID] = mark

    def printMark(self):
        print(f"Course: {self.course}:\n")
        for sID in self.__marks:
            print(f"{sID} -- {self.__marks[sID]}\n")

    def getMarkForStudent(self, sID):
        return self.__marks[sID]

    def getMark(self):
        return self.__marks


# Defining functions
