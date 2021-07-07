#!/usr/bin/python

import math 
import sys

if len(sys.argv)!=2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

r=int(sys.argv[1])          #파이썬은 문자로 받아오기 때문
pi=math.pi
result=round(r**2*pi,2)     #round(,2)->소수점 두자리 까지

print(result)


