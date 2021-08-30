with open("sequence.protein.2.fasta", "r") as fr:
    cnt = 0
    seq = ""
    for line in fr:
        if cnt == 0:
            title = line.strip()
        else:
            seq += line.strip()
        cnt += 1
print(f"title: {title}")
print(f"seq: {seq}")

# title: >AAB07223.1 BRCA2 [Homo sapiens]
# seq: MPIGSKERPT...QDTITTKKYI
