with open('p84.txt','r') as handle:
    cnt=1
    for i in handle:
        if not cnt%2:
            print(i.rstrip())
        cnt+=1

with open('p84.txt', 'r') as handle:
    for idx, i in enumerate(handle):
        if idx % 2 == 1:
            print(i.strip())
    
