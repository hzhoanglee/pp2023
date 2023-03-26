import input
import numpy as np

def listStudents():
    if len(input.students) < 1:
        print("There are no student")
        return
    print("List of Students:")
    for sID in input.students:
        input.students[sID].printInfo()
    print("====================")


def listCourses():
    if len(input.courses) < 1:
        print("There are no course")
        return
    print("List of Courses:")
    for s in input.courses:
        input.courses[s].printInfo()
    print("------------------")


def displayGPADescending():
    mark_array = np.empty((0, 2))
    input.calAllGPA()
    for student in input.students:
        sName = input.students[student].name()
        gpa = input.students[student].getGPA()
        mark_array = np.append(mark_array, [[sName, gpa]], axis=0)
    mark_array_sorted = mark_array[mark_array[:, 1].argsort()][::-1]
    for x in mark_array_sorted:
        print(f"Student: {x[0]} - GPA: {x[1]}")