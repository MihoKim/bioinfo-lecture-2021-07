#! /usr/bin/env python
"""
큰 수 출력하기 
num0 =5
num1 =7

if num0>num1:
    print(num0)
else:
    print(num1)

등급 지정하기 
i_Score=int(input('점수를 입력하시오: '))
if i_Score>=90:
    print('A')
elif int(i_Score)>=80:
    print('B')
elif int(i_Score)>=70:
    print('C')
elif int(i_Score)>=60:
    print('D')
else:
    print('F')
"""
"""
환율 계산기 1
i_USD=float(input('USD: '))
i_EUR=float(input('EUR: '))
i_JPY=float(input('JPY: '))
i_CNY=float(input('CNY: '))

if i_USD!=0:
    print('USD->KRW: ',i_USD*1203.82)
if i_EUR!=0:
    print('EUR->KRW: ',i_EUR*1365.73)
if i_JPY!=0:
    print('JPY->KRW: ',i_JPY*11.22)
if i_CNY!=0:
    print('CNY->KRW: ',i_CNY*172.04)
"""
"""
환율계산기 2
f_USD=float(input('USD: '))
f_EUR=float(input('EUR: '))
f_JPY=float(input('JPY: '))
f_CNY=float(input('CNY: '))
d_value = {
            'USD':1203.82,
            'EUR':1365.73,
            'JPY':11.22,
            'CNY':172.04
             }

KUSD=round(f_USD*d_value['USD'], 2)
KEUR=f_EUR*d_value['EUR']
KJPY=f_JPY*d_value['JPY']
KCNY=f_CNY*d_value['CNY']

print('USD->KRW is: {}'.format(KUSD))
print('EUR->KRW is: ' , KEUR)
print(f'JPY->KRW is: {KJPY}')
print(f'CNY->KRW is: {KCNY:.1f}')

"""
"""
환율계산기 3
inStr='10 USD,5 EUR,7 JPY,9 CNY'
d_value = {
            'USD':1203.82,
            'EUR':1365.73,
            'JPY':11.22,
            'CNY':172.04
             }
inStr = inStr.split(',')
Value0=inStr[0].strip().split()[0]
Type0=inStr[0].strip().split()[1]
Value1=inStr[1].strip().split()[0]
Type1=inStr[1].strip().split()[1]
Value2=inStr[2].strip().split()[0]
Type2=inStr[2].strip().split()[1]
Value3=inStr[3].strip().split()[0]
Type3=inStr[3].strip().split()[1]

print(Value0,Value1,Value2,Value3)
print(Type0,Type1,Type2,Type3)

Result0=int(Value0)*d_value[Type0]
Result1=int(Value1)*d_value[Type1]
Result2=int(Value2)*d_value[Type2]
Result3=int(Value3)*d_value[Type3]

print(Result0,Result1,Result2,Result3)


"""

"""

추가
if score.isdigit(): ------> to check if input value is a digit or not
    print("score", score, "is digit")
else:
    import sys
    sys.exit('asdf')
"""
