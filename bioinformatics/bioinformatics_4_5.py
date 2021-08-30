title_flag = False
l_title=[]
l_all=[]

with open("sequence.nucleotide.gb", "r") as fr:
    for line in fr:
        line = line.rstrip()
        if line.startswith("  TITLE"):
            title_flag = True
            l_title.append(line[12:])
        elif title_flag == True and line[0:12] == ' '*12:
            l_title.append(line[12:])
        elif line[0:12] != ' '*12 and len(l_title) != 0:
            title_flag = False
            l_all.append(' '.join(l_title))
            l_title=[]
    #print(l_title)
    print('  TITLE     ' + ('\n' + ' ' * 12).join(l_all))

            

# 타이틀 만나면 스위치 온, 내용을 담고, 일정 공백수 아니면 스위치 오프해서 담지 않는다.
