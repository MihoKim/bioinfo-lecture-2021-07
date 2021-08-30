num = int(input("Which times table: "))
if num < 1 or num > 9:  # 또는 if not 1<= num <=9:
    print("What?")
else:
    for i in range(1, 10):
        print(f"{num} * {i} = {num*i}")
