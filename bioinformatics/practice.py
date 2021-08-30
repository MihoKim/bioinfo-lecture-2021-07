fr = open("sequence.protein.gb", "r")
line_count = 0
title = ""
seq_list = list()
origin_flag = False
lines = fr.readlines()
for line in lines:
    line = line.strip()
    if line == "":
        continue
    if line_count == 0:
        title = line
    elif line[0:6] == "ORIGIN":
        origin_flag = True
    elif origin_flag == True:
        seq_list.append(line)
    line_count += 1
fr.close()

seq = "\n".join(seq_list)
print("title: %s" % (title))
print("seq: %s" % (seq))
