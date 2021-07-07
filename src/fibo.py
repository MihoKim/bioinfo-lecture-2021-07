# 재귀함수 - 피보나치수열

# import sys


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# n = int(sys.argv[1])
# print(fib(n))

import sys


def fib2(l, n):
    for i in range(n - 1):
        l.append(l[-1] + l[-2])
    return l


l = [0, 1]
n = int(sys.argv[1])
print(fib2(l, n))
print(l[n])
