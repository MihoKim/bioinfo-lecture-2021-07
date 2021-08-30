with open("sequence.protein.2.fasta", "r") as fr:
    cnt = 0
    seq = ""
    for line in fr:
        if cnt == 0:
            title = line.strip()
        else:
            seq += line.strip()
        cnt += 1

while True:
    pos = input("Position: ")
    if pos == "XXX":
        print("Okay, I will stop.")
        break
    else:
        pos = int(pos)
        aa = seq[pos - 1 : pos + 2]
        print(f"Three amino acids: {aa}")
