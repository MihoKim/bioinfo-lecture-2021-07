

file_name="write_sample.txt"

handle=open(file_name,'w')              #'w': 기존 내용이 삭제되고 새로운 내용 작성
handle.write("Hello\n")
handle.write("Bioinformatics\n")

with open(file_name, 'a') as handle:    #'a': 내용 추가
    handle.write("miho\n")

s = 's1,s2,s3'  #csv
data=s.split(',')
print(data)     #['s1', 's2', 's3']

with open(file_name,'a') as handle:
    handle.write('\t'.join(data))       #리스트의 요소들이 앞의 문자열과 합쳐져서 새로운 문자열로 반환됨



