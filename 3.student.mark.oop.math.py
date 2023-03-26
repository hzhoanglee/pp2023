from math import floor

import numpy
import numpy as np


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
def listStudents():
    if len(students) < 1:
        print("There are no student")
        return
    print("List of Students:")
    for sID in students:
        students[sID].printInfo()
    print("====================")


def listCourses():
    if len(courses) < 1:
        print("There are no course")
        return
    print("List of Courses:")
    for s in courses:
        courses[s].printInfo()
    print("------------------")


def assignMark(cID):
    cName = courses[cID].getName()
    print("Filling mark for course " + cName)
    for student in students:
        mark = float(input(f"Enter Mark for {students[student].name()}: "))
        marks[cID].newMark(students[student].id(), floor(mark))
        print("Done.")


def getMark(cID):
    cName = courses[cID].getName()
    print("Mark sheet for course " + cName)
    marks[cID].printMark()


def calGPA(sID, doPrint=True):
    studentMarks = np.array([])
    for course in courses:
        courseObj = courses[course]
        courseCredit = courseObj.getCredit()
        courseID = courseObj.getID()
        courseMark = marks[courseID].getMark()
        if sID in courseMark:
            singleCourseMark = float(courseMark[sID])
            for i in range(int(courseCredit)):
                studentMarks = np.append(studentMarks, singleCourseMark)
    gpa = floor(np.average(studentMarks) * 100) / 100.0
    students[sID].setGPA(gpa)
    if doPrint:
        print(f"GPA for student {students[sID].name()}: {gpa}")


def calAllGPA():
    for student in students:
        sID = students[student].id()
        calGPA(sID, False)


def displayGPADescending():
    mark_array = np.empty((0, 2))
    calAllGPA()
    for student in students:
        sName = students[student].name()
        gpa = students[student].getGPA()
        mark_array = np.append(mark_array, [[sName, gpa]], axis=0)
    mark_array_sorted = mark_array[mark_array[:, 1].argsort()][::-1]
    for x in mark_array_sorted:
        print(f"Student: {x[0]} - GPA: {x[1]}")


if __name__ == '__main__':
    # Read students
    number_of_students = 0
    students = {}
    while number_of_students <= 0:
        number_of_students = int(input("Input number of students in the class: "))
    for i in range(number_of_students):
        print("Student number " + str(i + 1))
        studentObj = Student()
        students[studentObj.id()] = studentObj
        print(f"Added Student {studentObj.name()}")

    # Read courses
    number_of_courses = 0
    marks = {}
    courses = {}
    while number_of_courses <= 0:
        number_of_courses = int(input("Input number of courses in the class: "))
    for i in range(number_of_courses):
        print("Course number " + str(i + 1))
        courseObj = Course()
        courses[courseObj.getID()] = courseObj
        marks[courseObj.getID()] = MarksByCourse(courseObj.getID())
        print(f"Added Course {courseObj.getName()}")

option_selected = -1
while option_selected != 0:
    print("===Marking Function===")
    print("1. Assign Mark")
    print("===Listing Function===")
    print("2. List Courses")
    print("3. List Students")
    print("4. Show student marks for a given course")
    print("5. Calculate GPA for a student")
    print("6. Print GPA in descending")
    print("0. Exit")
    option_selected = int(input("Select an option: "))
    if option_selected == 1:
        cID = int(input("Enter Course ID: "))
        assignMark(cID)
    elif option_selected == 2:
        listCourses()
    elif option_selected == 3:
        listStudents()
    elif option_selected == 4:
        cID = int(input("Enter Course ID: "))
        getMark(cID)
    elif option_selected == 5:
        sID = int(input("Enter Student ID: "))
        calGPA(sID)
    elif option_selected == 6:
        displayGPADescending()
    else:
        print("No such options. Please try again")
