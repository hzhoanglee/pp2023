from domains.student import Student
from domains.course import Course
from domains.mark_by_course import MarksByCourse
import numpy as np
from math import floor

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


prompt = input
