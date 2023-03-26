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