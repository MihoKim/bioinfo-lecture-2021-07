# 077.bed 파일을 조금 수정하여 각 chromosome 별로 구간의 길이를 계산해보세요.
result = 0
with open("077.bed", "r") as fr:
    for line in fr:
        data = line.strip().split("\t")
        # int(l_line[2]) - int(l_line[1])
        chrom, start, end = data
        length = int(end) - int(start)
        result += length
print(result)  # 29681
