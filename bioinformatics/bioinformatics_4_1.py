with open("sequence.protein.gb", "r") as fr:
    cnt = 0
    title = ""
    seq = ""
    for line in fr:
        if cnt == 0:
            title = line.strip()
        elif not line.startswith("ORIGIN"):
            continue
        else:
            for sub_line in fr:
                sub_line = sub_line.lstrip()
                seq += sub_line
        cnt += 1

print(f"title: {title}")
print(f"seq: {seq}")
