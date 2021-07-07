
'''
file_name="read_sample.txt"

with open(file_name, 'r') as handle:
    for line in handle:         #for문으로 iterable 파일 객체에 대해 한줄씩 읽을 수 있다
        print(line.strip())     #strip()으로 라인 끝의 줄바꿈 제거; 양쪽 끝의 white space 제거 가능
'''
'''
handle = open(file_name,'r')
for line in handle:
    print(line.strip())
handle.close()
'''
file_name="read_sample.txt"

with open(file_name, 'r') as handle:
    #print(type(handle))
    lines = handle.readlines()
    #print(type(lines))
    for line in lines:
        print(line.strip())
'''
handle=open(file_name,'r')
lines=handle.readlines()
for line in lines:
    print(line.strip())
handle.close()
'''
