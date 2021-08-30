#! /usr/bin/env python

'''
## for문 
l_range=[1,2,5,3,1,7]
for i in l_range:
    if i==1:        #indent required
        print(i)
    else:
        continue    #실행하지 않고 넘어감; 다시 for문 처음으로!
        #print('not 1!')
    print('current i:',i)

print('done!')
'''
'''
# range()
for i in range(5):  #for 문 5번 반복 
    print('*')

print(list(range(2,5,1)))       #[2, 3, 4]
print(list(range(5,1,-1)))      #[5, 4, 3, 2]
print(list(range(9)))           #[0, 1, 2, 3, 4, 5, 6, 7, 8]

totalSum=0
for i in range(3):
    totalSum+=i
    print(i)

print('totalSum:',totalSum)
'''
'''
# 내장함수 
for i, j in enumerate(['a','b','c']):   #[(0,'a'),(1,'b'),(2,'c')]
    print(i,j)
print(type(enumerate(['a','b','c'])))
'''
'''
# 구구단 출력하기 
gugu = input('gugu?')

for i in range(1,10):
    dan=int(gugu)*i
    print('{}*{}:'.format(gugu,i), dan)


gugu = input('gugu?')

while (not gugu.isdigit()):
    gugu=input('gugu is not digit!:')
gugu = int(gugu)
#gugu is integer
while not (2<=gugu<=19):
    gugu=input('[2,19]:')
gugu=int(gugu)
for i in range(1,10):
    dan=gugu*i
    print('{}*{}: {}'.format(gugu,i, dan))
'''
'''
# conditions and loops


total=0
for i in range(101,200,2):
    total+=i
print(total)                    #7500

myList=[]
for i in range(101,200):
    if i%2==1:
        myList.append(i)
print(sum(myList))              #7500

print(sum(range(101,200,2)))    #7500


inStr=input('a(space)b:')
a,b=inStr.split()

myList=[]
for i in range(int(a),int(b)):
    if i%2==1:
        myList.append(i)
print(sum(myList))
'''

## Palindromic sequence 판별

#방법1
inSeq=input('Give me Sequence!: ')
d_nuc1={'A':'T','T':'A','C':'G','G':'C'}

inSeq=inSeq.upper()
outSeq=''
for i in inSeq[::-1]:
    outSeq+=d_nuc1[i]
if (outSeq == inSeq):
    print('{} is palindromic.'.format(inSeq))
else:
    print('{} is not palindromic.'.format(inSeq))   

#방법2
inSeq=input('Give me Sequence!: ')
d_nuc1={'A':'T','T':'A','C':'G','G':'C'}

inSeq=inSeq.upper()
for i in range(len(inSeq)):
    if(inSeq[i]==d_nuc1[inSeq[-i-1]]):      #from reverse; 한글자씩 비교!
        print("Okay~")
    else:
        print("Not palindrom!")

#방법3
inSeq=input('Give me Sequence!: ')

inSeq=inSeq.upper()
outSeq=inSeq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[::-1]
if inSeq==outSeq:
    print(inSeq,'is palindromic')    
else:
    print(inSeq,'is not palindromic')

'''
inSeq=input('Give me Sequence!: ')

inSeq=inSeq.upper()
outSeq=inSeq.replace('A','T').replace('T','A').replace('G','C').replace('C','G')[::-1]
if outSeq == inSeq:
    print(inSeq,'is palindromic.')
else:
    print(inSeq,'is not palindromic.')
print(outSeq)
'''

'''
## Dictionaries

# DNA nucleotide: Complement
# 방법1
toCount='We tried list and we tried dicts also we tried Zen'
d_count=dict()

l_toCount=toCount.split()
for key in l_toCount:           #단어 리스트
    if key not in d_count:      #딕셔너리 키유무
        d_count[key]=1          #없으면 1
    else:
        d_count[key]+=1         #있으면 +1

for i in d_count:
    print(i, d_count[i])

for k, v in d_count.items():
    print(k,v)
    
# 방법2: library 이용
from collections import Counter
toCount='We tried list and we tried dicts also we tried Zen'

l_toCount=toCount.split()
cnt=Counter(l_toCount)
print(cnt)
cnt['tried']+=100
print(cnt)


# dictionary 활용
d_dict=dict()                               #create empty dictionary
if 'and' in d_dict: print('theres and!')    #check if keys in dictionary
d_dict.get('and')                           #get value from dictionary 

d_dict['and']=1                             #assign key-value pair for dict
if 'and' in d_dict: print('theres and!')    #check if keys in dictionary
d_dict.get('and')                           #get value from dictionary
d_dict['and']+=1                            #assign key-value pait for dict
'''

