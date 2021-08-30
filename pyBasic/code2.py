#! /usr/bin/env python

## list(리스트)

#l_test=[1,2,3,'apple',' ']
#l_test2=['a','b','c']

# 리스트 인덱싱, 슬라이싱
#print(l_test[0]+l_test[2])          #4; 1과 3을 더한 값
#print(l_test[1:])                   #[2, 3, 'apple', ' ']

# 리스트 연산
#print(l_test + l_test2)             #리스트와 리스트를 더하면, 하나의 리스트로 연결된다.
#print(l_test * 3)                   #리스트에 숫자를 곱한 만큼 하나의 리스트 반복된다.
#print(l_test * l_test2)            #리스트와 리스트는 곱할 수 없다(주의!)

#중첩리스트(리스트 안에 리스트)
#l_test1=[1,2,3,4,['a','b'],5]       
#print(l_test1)                      #[1, 2, 3, 4, ['a', 'b'], 5]
#print(l_test1[3:5])                 #[4, ['a', 'b']]; 3,4번째 index 값 출력

# 리스트 슬라이싱 
#numbers=[0,1,2,3,4,5,6,7,8,9,10]
#print("numbers[1]:", numbers[1])                #numbers[1]: 1
#print("numbers[-1]:", numbers[-1])              #numbers[-1]: 10 
#print("numbers[::-1]:", numbers[::-1])          #numbers[::-1]: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#print("numbers[::-2]:", numbers[::-2])          #numbers[::-2]: [10, 8, 6, 4, 2, 0]
#print("numbers[1:5:2]:", numbers[1:5:2])        #numbers[1:5:2]: [1, 3]
#print("numbers[-2:-6:-2]:", numbers[-2:-6:-2])  #numbers[-6:-2:-2]: [9, 7]

# 리스트 함수 
l_num=[0,1,2,3]
l_num.append(['a','b'])
print(l_num)                        #[0, 1, 2, 3, ['a', 'b']]
l_num.remove(['a','b'])             
print(l_num)                        #[0, 1, 2, 3]             
l_num.sort()
print(l_num)                        #[0, 1, 2, 3]
l_num.reverse()
print(l_num)                        #[3, 2, 1, 0]

l_num=[0,1,2,3,5,4]
print(l_num.index(5))               #4
print(l_num[4])                     #5
l_num.insert(2,['a','b'])           
print(l_num)                        #[0, 1, ['a', 'b'], 2, 3, 5, 4]
print(l_num.pop())                  #4 
print(l_num)                        #[0, 1, ['a', 'b'], 2, 3, 5]
print(l_num.pop(2))                 #['a','b']
print(l_num)                        #[0,1,2,3,5]

# 리스트 만들기
#lang0 = ['Python', 'JAVA']
#lang1 = ['C', 'C++', 'VB']

#totalLang = lang0 + lang1
#print(totalLang)            #['Python', 'JAVA', 'C', 'C++', 'VB']

#totalLang = lang0
#totalLang.extend(lang1)
#print(totalLang)            #['Python', 'JAVA', 'C', 'C++', 'VB']


## dictionary

#d_table = {'fruit':'apple','color':'red','dia':10}
#print(d_table['color'])

# 딕셔너리 활용 (문제)
regNum0 = '951213-0000000'
regNum1 = '960125-0000000'
regNum2 = '970705-0000000'

d_mon={'01':'Jan', '07':'Jul', '12':'Dec'}

print('regNum0:',d_mon[regNum0[2:4]]+"-"+regNum0[4:6])
print('regNum1:',d_mon[regNum1[2:4]]+"-"+regNum1[4:6])
print('regNum2:',d_mon[regNum2[2:4]]+"-"+regNum2[4:6])



d_dict = {
'a_str':'Apple!',
'b_list':[1,2,3,4],
'c_tuple':('a','b','c'),
'e_dict':{1:'one',2:'two'}
}

print('d_dict', d_dict)
print('d_dicta', d_dict['a_str'])
print('d_dictb', d_dict['b_list'])
print('d_dictb0', d_dict['b_list'][0])
print('d_dictb1', d_dict['b_list'][1])
print('d_dictb2', d_dict['b_list'][2])
print('d_dictb3', d_dict['b_list'][3])
print('d_dictc', d_dict['c_tuple'])
print('d_dicte', d_dict['e_dict'])
print('d_dicte', d_dict['e_dict'][2]) 





