# # 070.vcf 파일에서 #을 제외한 행의 개수를 구해보세요.
# cnt_all = 0
# with open("070.vcf", "r") as fr:
#     for line in fr:
#         if line.startswith("#"):
#             continue
#         cnt_all += 1
# print(cnt_all)  # 12

# # 070.vcf 파일에서 FILTER 열이 PASS인 행의 개수를 세어보세요.
# cnt_pass = 0
# with open("070.vcf", "r") as fr1:
#     for line in fr1:
#         if line.startswith("#"):
#             continue
#         data = line.strip().split("\t")
#         if data[6] == "PASS":
#             cnt_pass += 1
# print(cnt_pass)  # 5

cnt_all = 0
cnt_pass = 0

with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header = line.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue
        data = line.strip().split("\t")
        cnt_all += 1
        if data[filter_idx] == "PASS":
            cnt_pass += 1
print(cnt_pass, cnt_all, cnt_pass / cnt_all)
