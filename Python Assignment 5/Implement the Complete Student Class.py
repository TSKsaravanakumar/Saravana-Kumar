class Student:
    def __init__(self,Name=None,RollNumber=None):
        self.__Name = Name
        self.__RollNumber = RollNumber

    def setName(self,x):
        self.__Name=x
    def getName(self):
        return self.__Name
    def setRollNumber(self,x):
        self.__RollNumber=x
    def getRollNumber(self):
        return self.__RollNumber
a=Student()
a.setName("Saravana")
print(a.getName())
a.setRollNumber(30)
print(a.getRollNumber())