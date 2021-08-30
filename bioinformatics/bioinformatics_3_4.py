# 내 풀이
with open("sequence.protein.2.fasta", "w") as fw:
    with open("sequence.protein.fasta", "r") as fr:
        for line in fr:
            fw.write(line)

# 강사님 풀이
# fr = open('sequence.protein.fasta','r'):
# lines=fr.readlines()
# seq_list=list()
# for line in lines:
