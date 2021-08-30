# 두 개의 문자열 s1과 s2를 입력받아 s1의 길이가 홀수이고 s2보다 짧으면 s1, s2의 순서로 출력하고,
# 그렇지 않으면 반대 순서로 출력하는 프로그램을 완성하시오.

s1 = str(input("Enter s1: "))
s2 = str(input("Enter s2: "))

if len(s1) % 2 == 1 and len(s1) < len(s2):
    print(s1 + s2)
else:
    print(s2 + s1)
