import os


# Define Functions
def assignMark(cID):
    if cID not in courses:
        print("Cannot find such course")
        return
    else:
        courseToAccess = courses[cID]
        cName = courseToAccess['name']
    print("Filling mark for course " + cName)
    for x in students:
        tmpStudent = students[x]
        mark = int(input("Enter Mark for " + tmpStudent['name'] + ": "))
        if tmpStudent['id'] in studentMark:
            studentMark[tmpStudent['id']][cID] = mark
        else:
            newMark = {}
            studentMark[tmpStudent['id']] = newMark
            studentMark[tmpStudent['id']][cID] = mark
    print("Saved successfully!")


def getMark(cID):
    if len(studentMark) == 0:
        print("No student was marked")
        return
    if cID not in courses:
        print("Cannot find such course")
        return
    cName = courses[cID]['name']
    print("Marksheet for course " + cName)
    for x in studentMark:
        if cID in studentMark[x]:
            print("ID: " + str(x) + "\t " + "Name: " + students[x]['name'] + " \t Mark: " + str(studentMark[x][cID]))


def listCourses():
    if len(courses) < 1:
        print("There are no course")
        return
    print("List of Courses:")
    for x in courses:
        print("|ID: " + str(x) + " |\t " + "Name: " + courses[x]['name'])
    print("------------------")


def listStudents():
    if len(students) < 1:
        print("There are no student")
        return
    print("List of Students:")
    for x in students:
        print("|ID: " + str(x) + " |\t " + "Name: " + students[x]['name'] + " |\t " + "DOB: " + students[x]['dob'])
    print("------------------")


def clearScreen():
    os.system("Clear")


# Read from Keyboard
number_of_students = 0
students = {}
while number_of_students <= 0:
    number_of_students = int(input("Input number of students in the class: "))
for i in range(number_of_students):
    print("Student number " + str(i + 1))
    student = {'id': int(input("Enter Student ID: ")),
               'name': input("Enter Student name: "),
               'dob': input("Enter Student DOB: ")}
    students[student['id']] = student
    clearScreen()
    print("Added Student: " + student['name'])


number_of_courses = 0
courses = {}
while number_of_courses <= 0:
    number_of_courses = int(input("Input number of courses in the class: "))
for i in range(number_of_courses):
    print("Course number " + str(i + 1))
    course = {'id': int(input("Enter Course ID: ")),
              'name': input("Enter Course Name: ")}
    courses[course['id']] = course
    clearScreen()
    print("Added Course " + course['name'])

# Options
studentMark = {}
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
    clearScreen()
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