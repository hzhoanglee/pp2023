# Defining the classes
class Student:
    def __init__(self):
        self.__sId = int(input("Enter Student ID: "))
        self.__sName = input("Enter Student name: ")
        self.__sDOB = input("Enter Student DOB: ")

    def id(self):
        return self.__sId

    def name(self):
        return self.__sName

    def dob(self):
        return self.__sDOB

    def printInfo(self):
        print("------------------------")
        print(f"Student ID: {self.__sId}")
        print(f"Student Name: {self.__sName}")
        print(f"Student DOB: {self.__sDOB}")


class Course:
    def __init__(self):
        self.__cId = int(input("Enter Course ID: "))
        self.__cName = input("Enter Course Name: ")

    def id(self):
        return self.__cId

    def name(self):
        return self.__cName

    def printInfo(self):
        print("------------------------")
        print(f"Course ID: {self.__cId}")
        print(f"Course Name: {self.__cName}")


class MarksByCourse:
    def __init__(self, cID):
        self.course = cID
        self.__marks = {}

    def newMark(self, sID, mark):
        self.__marks[sID] = mark

    def printMark(self):
        print(f"Course: {self.course}\n:")
        for sID in self.__marks:
            print(f"{sID} -- {self.__marks[sID]}\n")


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
    cName = courses[cID].name()
    print("Filling mark for course " + cName)
    for student in students:
        mark = int(input(f"Enter Mark for {students[student].name()}: "))
        marks[cID].newMark(students[student].id(), mark)
        print("Done.")


def getMark(cID):
    cName = courses[cID].name()
    print("Marksheet for course " + cName)
    marks[cID].printMark()


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
        courses[courseObj.id()] = courseObj
        marks[courseObj.id()] = MarksByCourse(courseObj.id())
        print(f"Added Course {courseObj.name()}")

option_selected = -1
while option_selected != 0:
    print("===Marking Function===")
    print("1. Assign Mark")
    print("===Listing Function===")
    print("2. List Courses")
    print("3. List Students")
    print("4. Show student marks for a given course")
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
    else:
        print("No such options. Please try again")