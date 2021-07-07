import gzip

file_name='covid19.fasta.gz'

data=dict()                             #data={}

#with gzip.open(file_name, 'rb') as handle:
with gzip.open(file_name, 'rt') as handle:
    for line in handle:
        #line=line.decode("utf-8")
        if line.startswith(">"):
            continue                    #다시 (첫번째)for문 실행
        for base in line.strip():       #line의 각 문자에 대해 (두번째)for문 실행 
            if base not in data:
                data[base]=0            #data 딕셔너리에 key와 value를 추가해감
            data[base]+=1

print(data)



