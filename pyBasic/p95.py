class Student():
    def __init__(self, korean, english, math):
        self.__korean = korean
        self.__english = english
        self.__math = math
    def showKorean(self):
        print('Korean:',self.__korean)
    def showEnglish(self):
        print('English:',self.__english)
    def showMath(self):
        print('Math:',self.__math)
    def showEverage(self):
        print('Everage:',(self.__korean + self.__english + self.__math)/3)

import sys
yune = Student(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
yune.showKorean()
yune.showEnglish()
yune.showMath()
yune.showEverage()


