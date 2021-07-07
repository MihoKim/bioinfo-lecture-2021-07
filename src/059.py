# 059.fasta 파일의 염기 A, C, G, T의 개수를 세어보세요.
data = dict()
f = "059.fasta"

with open(f, "r") as fr:
    for line in fr:
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1

print(data)
