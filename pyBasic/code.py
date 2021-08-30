#! /usr/bin/env python


## String;single line('', "") with escape character(\)
#print("1_Hello, \'World!\'")  #escape(\); single quote(\') 
#print("2_Hello, \tWorld!")    #escape(\); horizontal tap key(\t)
#print("3_Hello, \nWorld!")    #escape(\); enter key(\n) 
#print("4_Hello, \rWorld!")    #escape(\); carriage return(\r)     
#print("5_123456789\n\r123456789")     #개행문자(\n\r); 다음 줄의 맨앞으로 커서 이동 


## multiple line(""" """) 
#print("""Hello,

#World!""") 


## 문자열 연산
#print("Hello, " + "World!")   #문자와 문자를 더하면, 문자가 연결된다.
#print("Hello, " * 5)          #문자에 숫자를 곱하면, 문자를 여러번 쓸 수 있다.
#print("Hello, " * "World!")   #문자와 문자는 곱할 수 없다.


## 문자열 인덱싱
#fruit = 'apple'     #변수 지정(index 0~4)
#print(fruit)        #변수 출력;apple
#print(fruit[3])     #index 3 출력;l
#print(fruit[1:3])   #index 1~3*전*까지 출력;pp  
#print(fruit[:3])    #index 처음(0)부터 3*전*까지 출력;app 
#print(fruit[1:4])   #index 1~4*전*까지 출력;ppl
#print(fruit[2:])    #index 2~끝(4)까지 출력;ple


## 문자열 슬라이싱
#A='red apple'
#B='yellow banana'
#yellow apple
#print(B[:6]+A[3:])
#red banana 
#print(A[:3]+B[6:])

#sample='HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
#Humpty Dumpty 
#print(sample[22:28]+" "+sample[97:103])
#print(sample[22:28],sample[97:103])
#print(sample[22:28], end=' ')
#print(sample[97:103])


## 문자열 포매팅
#cntApple=1
#print('there are %d apples.' % cntApple)
#cntApple=2
#print('there are %d apples.' % cntApple)
#cntApple=3
#print('there are %d apples.' % cntApple)
#cntApple=4
#print('there are %d apples.' % cntApple)
#print('-' * 30)

#fruit='apples'
#print('there are %s from %s trees.' % (fruit, fruit))
#fruit='peaches'
#print('there are %s from %s trees.' % (fruit, fruit))
#fruit='plums'
#print('there are %s from %s trees.' % (fruit, fruit))

#cnt=1
#print('there are {} apples.'.format(cnt))
#cnt='one'
#print('there are {} abc {}.'.format(cnt,'peaches'))

## 문자열 함수 
CMA = '1,234,567'
#1234667
print(int(CMA.replace(',',''))+100)

# DNA nucleotide: Count
DNA_seq='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
print(DNA_seq.count('A'), DNA_seq.count('C'), DNA_seq.count('G'), DNA_seq.count('T'))

# DNA nucleotide: Transcription
DNA2RNA='GATGGAACTTGACTACGTAAATT'
print(DNA2RNA.replace('T','U'))

