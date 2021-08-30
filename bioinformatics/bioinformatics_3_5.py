with open("sequence.protein.2.fasta", "r") as fr:
    cnt = 0
    for line in fr:
        line = line.strip()
        if cnt == 1:
            break
        cnt += 1
print(f"The second line is: {line}")
