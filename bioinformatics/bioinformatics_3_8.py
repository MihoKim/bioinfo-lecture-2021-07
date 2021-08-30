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
    aa = input("Searching for: ")
    if aa == "XXX":
        print("Okay, I will stop.")
        break
    else:
        aa_list = []
        for pos, i in enumerate(seq):
            if i == aa:
                aa_list.append(str(pos))

    aa_str = ", ".join(aa_list)
    print(f"Found at: {aa_str}")


# Searching for: Q
# Found at: 66, 73, 84, 92, 126, ..., 3350, 3361, 3394, 3398, 3409
