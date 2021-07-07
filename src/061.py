# 061.fastq 파일에서 리드와 염기의 개수를 세어보세요.
cnt = 0
data = dict()
with open("061.fastq", "r") as fr:
    for line in fr:
        if cnt % 4 == 0:  # header
            pass
        elif cnt % 4 == 1:  # base
            for base in line.strip():
                if base not in data:
                    data[base] = 0
                data[base] += 1
        elif cnt % 4 == 2:  # delimiter
            pass
        elif cnt % 4 == 3:  # qual
            pass
        cnt += 1

print(cnt / 4)  # 100.0
print(data)  # {'G': 2446, 'C': 2391, 'A': 2766, 'T': 2497}
