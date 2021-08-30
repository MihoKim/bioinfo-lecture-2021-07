in_file = input("Enter input file: ")
out_file = input("Enter ouput file: ")
print(
    "Option-1) Read a FASTA format DNA sequence file and make a reverse sequence file."
)
print(
    "Option-2) Read a FASTA format DNA sequence file and make a reverse complement sequence file."
)
print("Option-3) Convert GenBank format file to FASTA format file.")
opt = input("Select the option: ")

if opt == "1":
    with open(out_file, "w") as fw:
        with open(in_file, "r") as fr:
            seq = ""
            for line in fr:
                if line.startswith(">"):
                    title = line.strip() + "\n"
                else:
                    seq += line.strip()
            s_rev_seq = seq[::-1]
            rev_seq = ""
            cnt = 1
            for i in s_rev_seq:
                rev_seq += i
                if cnt % 70 == 0:
                    rev_seq += "\n"
                cnt += 1

            fw.write(title + rev_seq)

elif opt == "2":
    with open(out_file, "w") as fw:
        with open(in_file, "r") as fr:
            seq = ""
            for line in fr:
                if line.startswith(">"):
                    title = line.strip() + "\n"
                else:
                    seq += line.strip()

            comp_seq = ""
            comp_data = {"A": "T", "T": "A", "C": "G", "G": "C"}
            for i in seq:
                comp_seq += comp_data[i]

            s_rev_comp_seq = comp_seq[::-1]
            rev_comp_seq = ""
            cnt = 1
            for i in s_rev_comp_seq:
                rev_comp_seq += i
                if cnt % 70 == 0:
                    rev_comp_seq += "\n"
                cnt += 1

            fw.write(title + rev_comp_seq)

elif opt == "3":
    with open(out_file, "w") as fw:
        with open(in_file, "r") as fr:
            seq = ""
            for line in fr:
                if line.startswith("LOCUS"):
                    title = line.strip() + "\n"
                elif not line.startswith("ORIGIN"):
                    continue
                else:
                    for sub_line in fr:
                        seq += sub_line.strip()

            s_seq = ""
            for i in seq:
                if i.isalpha():
                    s_seq += i

            f_seq = ""
            cnt = 1
            for i in s_seq:
                f_seq += i
                if cnt % 70 == 0:
                    f_seq += "\n"
                cnt += 1

            fw.write(title + f_seq)
