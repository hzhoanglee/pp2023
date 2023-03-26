import input
import output

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
    option_selected = int(input.prompt("Select an option: "))
    if option_selected == 1:
        cID = int(input.prompt("Enter Course ID: "))
        input.assignMark(cID)
    elif option_selected == 2:
        output.listCourses()
    elif option_selected == 3:
        output.listStudents()
    elif option_selected == 4:
        cID = int(input.prompt("Enter Course ID: "))
        input.getMark(cID)
    elif option_selected == 5:
        sID = int(input.prompt("Enter Student ID: "))
        input.calGPA(sID)
    elif option_selected == 6:
        output.displayGPADescending()
    else:
        print("No such options. Please try again")
