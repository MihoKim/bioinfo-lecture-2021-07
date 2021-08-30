#! /usr/bin/env python

## 함수 
'''
def showHello():
    print("Hello")
   p return '1'

#print(showHello())

a=showHello()       #a=1
print("number?")
print(a)
'''

'''
def add(a,b):
    print('add',a,'and',b)
    print('%d + %d ='%(a,b),a+b)
    return a+b

result=add(3,4)
print('result:', result)
'''

'''
def add(a,b=3):
    return a+b

print(add(5))       #8; b->기본값인 3으로 할당된다.
'''

'''
def book_0(name, age, book1, book2):
    print('name: {0}, age: {1}'.format(name, age), end = ' ')
    print('book:',book1,book2)

def book_1(name, age, *books):
    print('name: {0}, age: {1}'.format(name, age),end =' ')
    print('book:', end=' ')
    for book in books:
        print(book, end=' ')
    print()

book_0('yune',5,'python','basic')               #name: yune, age: 5 book: python basic  
book_1('yune',5,'python','basic')               #name: yune, age: 5 book: python basic
book_1('yune',5,'python','basic','photo')       #name: yune, age: 5 book: python basic photo

#book_0('yune',5,'python','basic','photo')      #error
'''

'''
print('lambda:',(lambda a,b:a+b)(3,4))              #lambda: 7

def add(a,b): return(a+b)
print('add:', add(3,4))                             #add: 7
'''
'''
# 계산기 함수 만들기

def calc(num0,op,num1):
    print('{} {} {} ='.format(num0,op,num1), end=' ')
    num0=float(num0)
    num1=float(num1)
    if op == '+':
        return num0+num1                        #결과값 반환; 함수 진행이 끝남 
    elif op == '-':
        return num0-num1
    elif op == '*':
        return num0*num1 
    elif op == '/':
        return num0/num1      
print(calc(input('num0: '),input('op: '), input('num1: ')))
'''
'''
# 내장함수 이용하는 방법
num0=input('num0: ')
op=input('op: ')
num1=input('num1: ')
print(eval('{}{}{}'.format(num0,op,num1)))         #내장함수 이용, 변수 지정해서 만들어보자
'''

# 피보나치 수열
n_pivo=int(input('n_th pivo: '))
l_pivo=[0,1]                                    #n_th pivo: l_pivo[n]
print('len(l_pivo):', len(l_pivo))
'''
#Use list and .append
def pivo(n):
    while len(l_pivo) < n:                      #거짓일때까지 반복!
    #for i in range(n-len(l_pivo)):             #while 또는 for 문 사용           
        l_pivo.append(l_pivo[-1]+l_pivo[-2])
    print(l_pivo[-1])
    print(l_pivo)
pivo(n_pivo)
'''
#재귀함수 사용
def pivo_r(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return pivo_r(n-1)+pivo_r(n-2)
print('pivo_r:',pivo_r(n_pivo-1))

'''
d_pivo = dict()
def pivo_d(n):
    if n in d_pivo:
        return d_pivo[n]
    else:
        if d_pivo 
'''

# 변수 유효 범위

chicken=10                  #전역 변수

def countChicken(people):
    chicken=20              #지역변수(함수 안에서 변수 선언)
    chicken-=people
    print('{0} chicken remained.'.format(chicken))

def countChicken_global(people):
    global chicken
    chicken-=people
    print('{0} chicken remained.'.format(chicken))

print('chicken:', chicken)  #전역변수
countChicken(5)             #지역변수 사용, 전역변수 그대로
print('chicken:',chicken)   #전역변수
print()
print('chicken:',chicken)   #전역변수
countChicken_global(5)      #전역변수 수정
print('chicken',chicken)    #전역변수








