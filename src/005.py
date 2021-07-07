

import sys

if len(sys.argv)!=2:
    print(f"#usage: python {sys.argv[0]} [num1]")
    sys.exit()

num1 = int(sys.argv[1])
result="neither 3,7"

if num1%3==0 and num1%7==0:
    result="3,7"
elif num1%3==0:
    result=="3"
elif num1%7==0:
    result=="7"

print(result)
