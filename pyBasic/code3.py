#! /usr/bin/env python


## Set 
#setA = {2,4,6,8,10,12}
#setB = {9,3,12,6}

#print(setA & setB)          #{12, 6}
#print(setA | setB)          #{2, 3, 4, 6, 8, 9, 10, 12}
#print(setA - setB)          #{8, 2, 10, 4}
#print(setA ^ setB)          #{2, 3, 4, 8, 9, 10}

#setA.add(100)
#print(setA)                     #{2, 4, 100, 6, 8, 10, 12}
#setA.remove(100)                
#print(setA)                     #{2, 4, 6, 8, 10, 12}                    
#setA.update([14,16,18])
#print(setA)                     #{2, 4, 6, 8, 10, 12, 14, 16, 18}


## Boolean
#print(1<10)                     #True
#print(bool('aa'))               #True
#print(bool({}))                 #False
#print(bool(0))                  #False
#condition ='apple'
#print(bool(condition))          #True


## 사용자 입력
#myVar1 = input('Var1: ')

#if myVar1 == '1':
#    print('myVar1 is 1!')
#else: 
#    pass
#    #print('myVar1 isnt 1!')
#print('Good Bye!')

## 큰 수 출력하기
#num0=5
#num1=7
##출력: 7
#if num0>num1:
#    print(num0)
#else:
#    print(num1)

#print(num1) if num0>num1 else print(num1)

## if, elif, else 
#fruit = 'peach'
#if fruit == 'peach':
#    print('peach')
#if fruit == 'apple':
#    print('apple')
#else:
#    print('else~~~')

## 등급 지정하기
score = input('점수 입력: ')
if 90 <= int(score) <= 100:
    print('A')
elif 80 <= int(score) < 90:
    print('B')
elif 70 <= int(score) < 80:
    print('C')
elif 60 <= int(score) < 70:
    print('D')
else:
    print('F') 


score = int(input('score: '))

if (score<=100) and (score>=90):
    grade='A'
elif (score<90) and (score>=80):
    grade='B'
elif (score<80) and (score>=70):
    grade='C'
elif (score<70) and (score>=60):
    grade='D'
elif (score<60):
    grade='F'
else:
    grade = 'Incorrect score' 

print(grade)

#종료
score = input('score: ')
if score.isdigit():
    print("score:",score,"is digit!")
else:
    import sys
    sys.exit('bye~')
print('aaaa') 
   








