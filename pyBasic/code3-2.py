#! /usr/bin/env python

## 환율 계산기
inStr = '10 USD, 5 EUR, 7 JPY, 9 CNY'
#inStr = 
#'
#10 USD
#,
# 5 EUR
#,
# 7 JPY
#,
# 9 CNY'
                   
d_value = {'USD':1203.82, 'EUR':1365.73, 'JPY':11.22,'CNY':172.04}

inStr = inStr.split(',')                            #type: string -> list
print(inStr)                                        #['10 USD', ' 5 EUR', ' 7 JPY', ' 9 CNY']

VALUE0=inStr[0].strip().split()[0]
TYPE0=inStr[0].strip().split()[1]
VALUE1=inStr[1].strip().split()[0]
TYPE1=inStr[1].strip().split()[1]
VALUE2=inStr[2].strip().split()[0]
TYPE2=inStr[2].strip().split()[1]
VALUE3=inStr[3].strip().split()[0]
TYPE3=inStr[3].strip().split()[1]

print(VALUE0, VALUE1, VALUE2, VALUE3)               #10 5 7 9
print(TYPE0, TYPE1, TYPE2, TYPE3)                   #USD EUR JPY CNY

RESULT0=str(round(int(VALUE0)*d_value[TYPE0],1))    
RESULT1=str(int(VALUE1)*d_value[TYPE1])
RESULT2=str(int(VALUE2)*d_value[TYPE2])
RESULT3=str(int(VALUE3)*d_value[TYPE3])

print(RESULT0, RESULT1, RESULT2, RESULT3)           #12038.2 6828.65 78.54 1548.36

outStr=' KRW, '.join([RESULT0, RESULT1, RESULT2, RESULT3])+' KRW'
print(outStr)                                       #12038.2 KRW, 6828.65 KRW, 78.54 KRW, 1548.36 KRW


## while 문

# 1부터 50까지 출력
#i=1
#while True:                         
#    print('loop test: '+str(i))
#    i += 1
#    if 50<i:
#        break

# 삼각형 그리기
#i=1
#while True:
#    print('*'*i)
#    i += 1
#    if i>6:    
#        break
i=1
star=''
while True:
    print(star)
    star+='*'
    i+=1
    if 7<i:
        break

# 정삼각형 그리기
i=1
j=5
while True:
    print(' '*j+'*'*i)
    i+=2
    j-=1
    if i>11:
        break

maxNum=int(input('odd number: '))
i=1
j=int((maxNum-1)/2)
while i<=maxNum:
    print(' '*j+'*'*i)
    i+=2
    j-=1
 





