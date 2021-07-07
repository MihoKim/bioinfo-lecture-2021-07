class A:
    def __init__(self, val):
        self.val=val
    
    def __add__(self,other):    
        return self.val+other.val
    
    def __mul__(self,other):
        return "__mul__" 
    
a1=A('a')
a2=A('b')

print(a1.val+a2.val)        #ab
print(a1+a2)                #클래스의 인스턴스끼리 더하기 -> __add__
                            #self: a1, other: a2로 a1.val+a2.val이 된다.
print(a1*a2)                #클래스의 인스턴스끼리 곱하기 -> __mul__




