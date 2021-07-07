#1
'''
import sys

try: 
    with open("noname.txt",'r') as fr:      #없는 파일을 읽으려고 하면 오류가 남
        read = fr.readlines()
except FileNotFoundError as err:            #오류를 발생시킨다음, 해당 오류를 잡기위해 오류이름을 적어준다.
    print("파일이 없습니다")
    # 또는 naname.txt 파일을 생성하는 과정 
    sys.exit()

print(read)
'''

#2
'''
import sys

try:
    num = int(input("Enter: "))
except ValueError as err:
    print(err)
    sys.exit()

try:
    print(10 / num)
except ZeroDivisionError as err:
    print(err)
    sys.exit()
'''

import sys

try:
    num=int(input("Enter: "))
    print(10/num)
except ValueError as err1:
    print(err1)
    sys.exit()
except ZeroDivisionError as err2:
    print(err2)
    sys.exit()



         


