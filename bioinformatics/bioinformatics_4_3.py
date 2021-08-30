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

s_seq = ""
for s in seq:
    if s.isalpha():
        s_seq += s

f_seq = ""
s_cnt = 1
for i in s_seq:
    f_seq += i
    if s_cnt % 70 == 0:
        f_seq += "\n"
    s_cnt += 1
print(f_seq)
