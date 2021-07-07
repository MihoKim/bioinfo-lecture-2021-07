class ValueCalculator:
    def __init__(self,val:str):
        self.val=val

    def __add__(self,other):
        return self.val+other.val 

if __name__=="__main__":        #이 파일을 실행할때만 실행, import로 불러올때는 실행되지 않음!!
    print('hi')        


