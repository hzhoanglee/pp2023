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