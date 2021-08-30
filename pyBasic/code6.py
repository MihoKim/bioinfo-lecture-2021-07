#! /usr/bin/env python

'''
# 파일 입출력
f = open('./p84.txt','r')
for i in f.readlines()[1::2]:
    print(i.replace('\n',''))
f.close()
'''
# 원의 면적 구하는 함수 만들기
def area(r):
    print(2*int(r)*3.141592)
area(input("r:"))
