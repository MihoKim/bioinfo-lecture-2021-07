# 내 풀이
with open("title.txt", "r") as fr:
    for line in fr:
        print(f"The first line is: {line}")

# 강사님 풀이
fr = open("title.txt", "r")
for line in fr:
    line.strip()
    break
fr.close()
print(f"The first line is: {line}")
