#! /usr/bin/env python

## 파일 입출력

'''
# 파일 읽기
FILE = open('./test.txt','r')

for i in FILE.readlines(): 
    print(i.strip().split()[0]) 

FILE.close()


# 파일 쓰기
FILE=open('./write.txt','w')        #'w'로 열면, 기존 파일 내용이 사라짐

for i in ['I','like','apple']:
        FILE.write(i+' ')           

FILE.write('\n')

FILE.close()
'''
'''
with open('./test.txt','r') as FI, open('./write.txt', 'w') as FO:  #with 안의 실행코드가 끝나면, open한 파일을 close해줌 
    for i in FI.readlines():
        FO.write(str(i))
        print(i.strip())
    print('with out! BYE!')
'''
'''
import pickle 

l_list=[1,3,5,7]
d_dict={'a':'A','b':'B',1:3,2:4}

F0=open('./pi','wb')
pickle.dump(l_list,F0)
pickle.dump(d_dict,F0)
F0.close()
'''

## 클래스
'''
class Person:
    nation='A nation'
    def greeting(self):
        print('(method)greeting:', 'Hi')
    def hi1(self):
        self.greeting()
    def hi2(self):
        greeting()

def greeting():
    print('(function)greeting:', 'Hello!')

yune=Person()
yune.greeting()
print()
yune.hi1()
yune.hi2()
'''

class Person:
    nation='A nation'
    def greeting(self,a):
        a.hi2()
        print('(method)greeting:', 'Hi')
    def hi1(self):
        self.greeting()
    def hi2(self):
        greeting()

def greeting():
    print('(function)greeting:', 'Hello!')

yune=Person()
yune1=Person()
yune.greeting(yune1)


'''
# init          

class Person:
    def __init__(self, in_nation):
        self.nation=in_nation
   
    def showNation(self):
        print(self.nation) 

yune=Person('Korea')
yune1=Person('AAA')

yune.showNation()                   #Korea
yune1.showNation()                  #AAA
'''
'''
# 상속
class Cat:
    def __init__(self):
        self.sleepy=True

    def snack(self):
        print('myeo~')

class KoShort(Cat):                 #상속(자식클래스: KoShort, 부모클래스: Cat) 
    def snack(self):                #메소드 오버라이딩 
        print("야옹")

catcat=Cat()                        #catcat은 부모클래스 Cat의 인스턴스
catcat.snack()                      #myeo~
print(catcat.sleepy, end='\n\n')    #True

minyong=KoShort()                   #minyong은 자식클래스 KoShort의 인스턴스 
minyong.snack()                     #야옹; 새로 정의한 자식클래스의 메소드를 사용 
print(minyong.sleepy)               #True; 부모클래스의 메소드를 사용
'''
'''
# 비공개속성 
class Cat:
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def setAge(self, Age):
        self.__age=Age
        print("set age to {0}.".format(Age))
    def showAge(self):
        print("{0} years old.".format(self.__age))
    def snack(self):
        print("야옹")

minyong=KoShort()
minyong.setAge(7)               #set age to 7.
minyong.snack()                 #야옹
minyong.showAge()               #7 years old.
#print(minyong.__age)           #Attribute error
'''
'''
class Cat:
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def setAge(self, Age):
        self.age=Age
        print("set age to {0}.".format(Age))
    def showAge(self):
        print("{0} years old.".format(self.age))
    def snack(self):
        print("야옹")

minyong=KoShort()
minyong.setAge(7)               #set age to 7.
minyong.snack()                 #야옹
minyong.showAge()               #7 years old.
print(minyong.age)           #Attribute error
'''

# 예외처리 

print('Try:')
try: 
    print("aaaaaa")
    print("aaaaaa")
    print(minyong.__age) 
    print("bbbbbb")
    print("bbbbbb")

except:
    print("Error!")

print("Done!")
